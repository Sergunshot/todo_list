from django import forms

from todo.models import Task, Tag


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
