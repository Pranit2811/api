from django.db import models
from django.core.exceptions import ValidationError
class Item(models.Model):
    id= models.AutoField(primary_key=True)
    item= models.CharField(max_length=20,)
    status = models.CharField(default='pending',max_length=20)
    