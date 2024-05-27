from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from myfirsttodoapp.models import ToDoApp
from django.utils import timezone
from datetime import date,timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def home(request):
    return render(request,'todoapp/home.html')

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

    paginator = Paginator(dataf,3)  # Show 4 tasks per page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)

    total = len(dataf)
    tomorrow = date.today() + timedelta(days=1)

    for data in dataf:
        if data.due_date and data.due_date == tomorrow:
            messages.warning(request, f"The task '{data.task}' is due on {tomorrow.strftime('%d/%m/%Y')}.")
            #return redirect('myfirsttodoapp:task')
        elif data.due_date and data.due_date == date.today():
            messages.warning(request, f"The task '{data.task}' is due today.")
            #return redirect('myfirsttodoapp:task')
        
    completed_task = ToDoApp.objects.filter(user=request.user, is_task_completed=True)
    completed_total = len(completed_task)
    
    return render(request, 'todoapp/index.html', {'dataf': dataf, 'total_count': total, 'completed': completed_total, "page_obj": page_obj})

@login_required
def update_task(request,task_id):
    #retrieving data from database
    update_data = ToDoApp.objects.get(id=task_id,user=request.user)
    
    print(f"from update function -- {update_data} {update_data.priority} {update_data.due_date}")

    #getting updated deails from html form and pushing it to database
    if request.method == 'POST':
        update_task = request.POST.get('update_taskname') 
        update_priority = request.POST.get('update_priority') 
        update_due_date = request.POST.get('update_due_date') 
        
        instance = update_data
        instance.task = update_task
        instance.priority = update_priority
        instance.due_date = update_due_date
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

