from django.urls import path, re_path
from . import views

app_name = 'references'

urlpatterns = [
    re_path('^tag/(?P<tag_name>[\w\W\s]+)/', views.tag, name='tag'),
    re_path('^search/', views.search, name='search'),
    re_path('^unique/(?P<id>[0-9]+)/', views.unique, name='unique'),
]