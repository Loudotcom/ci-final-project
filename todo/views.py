from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .forms import TaskForm
from .models import Task

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# class Tasks(generic.ListView):
#     model = Task
#     template_name = 'task_list.html'

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm() 
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_list.html'
    success_url = reverse_lazy('task_list')

    def TaskCreateView(request):
        form = TaskForm()
        context = {'form': form}
        return render(request, 'task_list.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return render(request, 'task_list.html', context)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = context['tasks'].filter(user=self.request.user)
    #     context['count'] = context['tasks'].filter(status=self.request.status).count()

    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['tasks'] = context['tasks'].filter(
    #             name__startswith=search_input)
    #     context['search_input'] = search_input
    #     return context


# class TaskDetail(LoginRequiredMixin, DetailView):
#     model = Task
#     context_object_name = 'task'
#     template_name = 'base/task.html'


# class TaskCreate(LoginRequiredMixin, CreateView):
#     model = Task
#     fields = ['name', 'notes', 'status']
#     success_url = reverse_lazy('tasks')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(TaskCreate, self).form_valid(form)


# class TaskUpdate(LoginRequiredMixin, UpdateView):
#     model = Task
#     fields = ['name', 'notes', 'status']
#     success_url = reverse_lazy('tasks')


# class TaskDeleteView(LoginRequiredMixin, DeleteView):
#     model = Task
#     context_object_name = 'task'
#     success_url = reverse_lazy('tasks')