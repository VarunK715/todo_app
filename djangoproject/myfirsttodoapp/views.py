from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from myfirsttodoapp.models import ToDoApp
from django.utils import timezone




def home(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')  # Access input data from POST request
        data = ToDoApp(task=task_name)
        data.save()
        return redirect('home')
    
    #Fetching data from databases
    dataf = ToDoApp.objects.all()
    total = len(dataf)

    #fetching completed task from db
    completed_task = ToDoApp.objects.filter(is_task_completed = True)
    completed_total = len(completed_task)
    
    return render(request,'index.html',{'tasks':dataf,'total_count':total,'completed':completed_total})


def update_task(request,task_id):
    #retrieving data from database
    update_data = ToDoApp.objects.get(id=task_id)
    

    #getting updated deails from html form and pushing it to database
    if request.method == 'POST':
        update_task = request.POST.get('update_taskname') 
        instance = ToDoApp.objects.get(id=task_id)
        instance.task = update_task
        instance.save()
        return redirect('home')

    return render(request,'update.html',{'data':update_data,'taskid':task_id})


def delete_task(request,task_id):
    task = get_object_or_404(ToDoApp, id=task_id)
    task.delete()
    return redirect('home')

def mark_as_completed(request):
    if request.method == "POST":
        completed_task = request.POST.getlist('completed')
        already_completed_tasks = ToDoApp.objects.filter(is_task_completed=True).values_list('id', flat=True)
        
        # Filter out the tasks that have already been marked as completed
        new_completed_tasks = [task for task in completed_task if int(task) not in already_completed_tasks]
        
        completion_time = timezone.now()
        print(f"task id -- {completed_task}")
        for taskid in new_completed_tasks:
            print(f"task id -- {taskid}")
            task = ToDoApp.objects.get(id=taskid)
            task.is_task_completed = True
            task.completed_task_at =completion_time
            task.save()
        completed_task.clear()
        return redirect('home')
    return redirect('home')
