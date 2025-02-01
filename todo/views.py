from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["__all__"]
    success_url = reverse_lazy("todo_list.html")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["__all__"]
    success_url = reverse_lazy("todo_list.html")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = ["__all__"]
    success_url = reverse_lazy("todo_list.html")
