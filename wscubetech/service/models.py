from django.db import models
class Service(models.Model):
    service_icom=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_des=models.TextField()

# Create your models here.
