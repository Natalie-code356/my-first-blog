from django.urls import path
from . import views
name='post_list'

urlpatterns = [
    path('', views.post_list, name='post_list'),
]