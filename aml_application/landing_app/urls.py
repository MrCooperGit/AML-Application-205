from django.urls import path, include
from landing_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'landing_app'

urlpatterns = [
    # all paths preceded by landing/
    path('', views.landing, name='landing'),
    path('<str:app_name>/', views.index, name='app_index'),
    path('tab/add/<str:app_name_to_add>/', views.add_tab, name='add_tab'),
    path('tab/delete/<str:tab_to_delete>/',
         views.delete_tab, name='delete_tab'),
]
