from django.urls import path
from .views import post_view
from .views import index

urlpatterns = [
    path('post/', post_view, name='post_view'),
    path('', index, name='index'),

]
