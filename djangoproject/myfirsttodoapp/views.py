from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from myfirsttodoapp.models import ToDoApp
from django.utils import timezone
from datetime import date,timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request,'todoapp/home.html')


# class About(LoginRequiredMixin,TemplateView):
#     template_name="todoapp/about.html"

@login_required
def task(request):
    if request.method == 'POST':
        if 'task' in request.POST:
            # Handle adding a new task
            task_name = request.POST.get('task')
            priority = request.POST.get('priority')
            due_date = request.POST.get('due_date')
            data = ToDoApp(task=task_name, user=request.user, priority=priority, due_date=due_date)
            data.save()
            return redirect('myfirsttodoapp:task')
        elif 'priority_sort' in request.POST:
            # Handle sorting by priority
            priority_sort = request.POST.get('priority_sort')
            dataf = ToDoApp.objects.filter(priority=priority_sort, user=request.user)
        elif 'search' in request.POST:
            # Handle sorting by priority
            keyword_search = request.POST.get('search')
            dataf = ToDoApp.objects.filter(task__icontains=keyword_search, user=request.user)
        else:
            dataf = ToDoApp.objects.filter(user=request.user)
    else:
        dataf = ToDoApp.objects.filter(user=request.user)

    total = len(dataf)
    tomorrow = date.today() + timedelta(days=1)

    for data in dataf:
        if data.due_date and data.due_date == tomorrow:
            messages.warning(request, f"The task '{data.task}' is due on {tomorrow.strftime('%d/%m/%Y')}.")
        elif data.due_date and data.due_date == date.today():
            messages.danger(request, f"The task '{data.task}' is due today.")
        
    completed_task = ToDoApp.objects.filter(user=request.user, is_task_completed=True)
    completed_total = len(completed_task)
    
    return render(request, 'todoapp/index.html', {'tasks': dataf, 'total_count': total, 'completed': completed_total})


@login_required
def update_task(request,task_id):
    #retrieving data from database
    update_data = ToDoApp.objects.get(id=task_id,user=request.user)
    

    #getting updated deails from html form and pushing it to database
    if request.method == 'POST':
        update_task = request.POST.get('update_taskname') 
        instance = update_data
        instance.task = update_task
        instance.save()
        return redirect('myfirsttodoapp:task')

    return render(request,'todoapp/update.html',{'data':update_data,'taskid':task_id})

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(ToDoApp, id=task_id,user=request.user)
    task.delete()
    return redirect('myfirsttodoapp:task')

@login_required
def mark_as_completed(request):
    if request.method == "POST":
        completed_task = request.POST.getlist('completed')
        already_completed_tasks = ToDoApp.objects.filter(user=request.user,is_task_completed=True).values_list('id', flat=True)
        
        # Filter out the tasks that have already been marked as completed
        new_completed_tasks = [task for task in completed_task if int(task) not in already_completed_tasks]
        completion_time = timezone.now()
       
        for taskid in new_completed_tasks:
            task = get_object_or_404(ToDoApp, id=taskid, user=request.user)
            task.is_task_completed = True
            task.completed_task_at =completion_time
            task.save()
        completed_task.clear()
        return redirect('myfirsttodoapp:task')
    return redirect('myfirsttodoapp:home')
