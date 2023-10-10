from django.urls import path
from . import views

urlpatterns = [
    path('generate_pdf/', views.GeneratePDF.as_view(), name='generate_pdf'),
    path('view_pdf/', views.view_pdf, name='view_pdf'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
    path('form/', views.customer_due_diligence_view, name='form')
]
