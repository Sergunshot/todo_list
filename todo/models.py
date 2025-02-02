from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=250, null=False)
    task_create = models.DateTimeField(null=False, auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    decision = models.BooleanField(default=False, null=False)
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["decision", "task_create"]
