from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:app_name>/', views.index, name='app_index')
]
