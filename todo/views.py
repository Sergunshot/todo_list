from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TodoForm, TagForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TodoForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todo:todo-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TodoForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todo:todo-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = ["__all__"]
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("todo:todo-list")


class TagListView(generic.ListView):
    model = Tag
    fields = ["__all__"]
    template_name = "tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = ["__all__"]
    template_name = "tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


def change_status(request: HttpRequest, pk) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    if task.decision:
        task.decision = False
        task.save()
    else:
        task.decision = True
        task.save()

    return HttpResponseRedirect(reverse_lazy("todo:todo-list"))
