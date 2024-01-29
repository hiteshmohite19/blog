from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','status')

admin.site.register(Blog,BlogAdmin)