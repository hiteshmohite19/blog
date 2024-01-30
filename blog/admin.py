from django.contrib import admin
from .models import Blog, Comment

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "status")


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "status")
    search_fields = ("name", "post", "slug")
    list_filter = ("publish", "status")


admin.site.register(Comment, CommentAdmin)
