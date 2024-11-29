from django.urls import path
from . import views

urlpatterns = [
    path('', 
        views.Task.as_view(), name='task_list'),
]