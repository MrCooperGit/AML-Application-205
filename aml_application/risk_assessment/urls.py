from django.urls import path
from risk_assessment import views

urlpatterns = [
    # all paths preceded by risk/
    path('home/', views.home, name='home'),
    path('risk-assess/', views.risk_assessment_view, name='risk_assessment_view'),

]
