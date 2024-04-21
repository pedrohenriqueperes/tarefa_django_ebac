from django.urls import path
from .views import post_view

urlpatterns = [
    path('post/', post_view, name='post_view'),
]
