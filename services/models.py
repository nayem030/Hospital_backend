from django.db import models

# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=30)
    descriptions=models.TextField()
    image=models.ImageField(upload_to="services/images")
