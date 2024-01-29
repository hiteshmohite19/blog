from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
# Create your models here.

class Blog(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='published')

    options = (
        ("default", "Default"),
        ("published", "Published"),
    )

    title = models.CharField(blank=False, null=False, max_length=50)
    slug = models.SlugField(unique_for_date="publish")
    publish = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    content = models.TextField(blank=False, max_length=50)
    status = models.CharField(choices=options, max_length=50)
    objects = models.Manager()
    new_manager = NewManager()

    def get_absolute_url(self):
        return f'/blog/{self.slug}'

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title