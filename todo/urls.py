from django.urls import path
from . import views
from .views import TaskList, TaskCreateView, TaskUpdate

urlpatterns = [
    path('', 
        views.TaskList.as_view(), name='task_list'),
        path('create/', TaskCreateView.as_view(), name='task_create'),
        path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
        path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]