from django.urls import path
from risk_assessment import views
from base_app import views as base_views

app_name = 'risk_assessment'

urlpatterns = [
    # all paths preceded by risk/
    path('home/', views.home, name='home'),
    path('risk-assess/', views.risk_assessment_view, name='risk_assessment_view'),
    path('login/', base_views.login, name='login'),
]
