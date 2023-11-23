from django.urls import path
from . import views
from base_app import views as base_views


app_name = 'cdd'

urlpatterns = [
    # all paths preceded by cdd/
    path('register/', views.customer_due_diligence_view, name='register'),
    path('verify/', views.customer_verification_view, name='verify'),
    path('login/', base_views.login, name='login'),
    path('customer_list/', views.customer_list_view, name='customer_list'),
    path('update/<int:customer_id>/',
         views.update_customer_view, name='update_customer'),
    path('create_company/', views.create_company,
         name='create_company_view'),
    # test paths for tabs
]
