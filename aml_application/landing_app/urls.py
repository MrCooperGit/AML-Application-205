from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:app_name>/', views.index, name='app_index'),
    path('tab/add/<str:app_name_to_add>/', views.add_tab, name='add_tab'),
    path('tab/delete/<str:tab_to_delete>/', views.delete_tab, name='delete_tab'),
]