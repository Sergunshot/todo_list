from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo.forms import TaskCreationForm, TagForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todo:todo-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreationForm
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


class TaskSetStatusView(generic.DetailView):
    model = Task

    def post(self, request, **kwargs):
        self.object = self.get_object()
        self.object.decision = not self.object.decision
        self.object.save()
        return HttpResponseRedirect(reverse("todo:todo-list"))
