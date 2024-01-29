from django.urls import path
from .views import home, single_blog

urlpatterns = [
    path('',home),
    path('<slug:blog>',single_blog)
]