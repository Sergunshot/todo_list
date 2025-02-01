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
    success_url = reverse_lazy("todo_list.html")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TodoForm
    success_url = reverse_lazy("todo_list.html")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = ["__all__"]
    success_url = reverse_lazy("todo_list.html")


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
