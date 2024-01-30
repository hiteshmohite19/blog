from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from common.BaseModel import BaseModel

# Create your models here.


class Blog(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status="published")

    options = (
        ("default", "Default"),
        ("published", "Published"),
    )

    title = models.CharField(blank=False, null=False, max_length=50)
    slug = models.SlugField(unique_for_date="publish",blank=True)
    publish = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    content = models.TextField(blank=False, max_length=50)
    status = models.CharField(choices=options, max_length=50)
    objects = models.Manager()
    new_manager = NewManager()

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    comment = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return self.comment
