from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^technology/$', views.technology, name='technology'),
    re_path(r'^politics/$', views.politics, name='politics'),
    re_path(r'^sports/$', views.sports, name='sports'),
    re_path(r'^entertainment/$', views.entertainment, name='entertainment'),
]