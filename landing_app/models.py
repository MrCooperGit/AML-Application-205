from django.db import models
from base_app.models import AvailableApps, Entity, UserProfile
from django.contrib.auth.models import User

# Create your models here.

class UserTab(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_id = models.ForeignKey(AvailableApps, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    # session_id in future will hold session for saving form state
