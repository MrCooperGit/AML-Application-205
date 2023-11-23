from django.urls import path
from . import views

app_name = 'risk_assessment'

urlpatterns = [
    # all paths preceded by risk/
    path('home/', views.home, name='home'),
    path('view/', views.risk_assessment, name='view'),
    path('risk-assess/', views.risk_assessment_view, name='risk-assessment-view'),
    path('risk-pdf/', views.pdf_view, name='risk-pdf'),

]
