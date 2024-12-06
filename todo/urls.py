from django.urls import path
from . import views
from .views import TaskList, TaskCreateView

urlpatterns = [
    path('', 
        views.TaskList.as_view(), name='task_list'),
        path('create/', TaskCreateView.as_view(), name='task_create'),
]