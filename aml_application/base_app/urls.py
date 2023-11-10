from django.urls import path
from base_app import views

app_name = 'base_app'

urlpatterns = [
    # all paths preceded by base/. When calling urls use the app_name :function. E.g url for 'base_app:login'
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register-user/', views.register_user, name='register-user'),
    path('login/', views.custom_login_view, name='login'),
    path('index/', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
]
