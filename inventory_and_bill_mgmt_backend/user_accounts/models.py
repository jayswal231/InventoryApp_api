from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


def secondary_email_json():
    return {"secondary_email":[]}

class CustomUser(AbstractUser):
    
    uuid  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    date_of_birth = models.DateField(null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100, null=True)
    secondary_email = models.JSONField(default=secondary_email_json,null=True)
    
    def __str__(self):
        return self.first_name + " - username" + self.username + " " + self.last_name
    

    
class Staff(models.Model):
    staff_uuid  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)  
