
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('update/<int:task_id>/',views.update_task,name='update_task'),
    path('delete/<int:task_id>/',views.delete_task,name='delete_task'),
    path('completed/',views.mark_as_completed,name='mark_as_completed'),

]
