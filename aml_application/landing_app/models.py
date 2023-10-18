from django.db import models
from base_app.models import AvailableApps, Entity, UserProfile


# Create your models here.
class Active_Session(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.id

class UserTab(models.Model):
    id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Active_Session, on_delete=models.CASCADE)
    app_id = models.ForeignKey(AvailableApps, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    
    