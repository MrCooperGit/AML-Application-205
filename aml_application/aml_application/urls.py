from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base_app import views

urlpatterns = [
    path('base/', include('base_app.urls')),
    path('cdd/', include('customer_due_diligence.urls')),
    path('risk/', include('risk_assessment.urls')),
    path('landing/', include('landing_app.urls')),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
