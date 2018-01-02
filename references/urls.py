from django.urls import path, re_path
from . import views

app_name = 'references'

urlpatterns = [
    path('search/', views.Search.as_view(), name='search'),
]