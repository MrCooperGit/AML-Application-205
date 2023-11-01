from django.urls import path
from . import views
from base_app import views as base_views


app_name = 'cdd'

urlpatterns = [
    # all paths preceded by cdd/
    path('generate_pdf/', views.GeneratePDF.as_view(), name='generate_pdf'),
    path('view_pdf/', views.view_pdf, name='view_pdf'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
    path('register/', views.customer_due_diligence_view, name='register'),
    path('verify/', views.customer_verification_view, name='verify'),
    path('login/', base_views.login, name='login'),
]
