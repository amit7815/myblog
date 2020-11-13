from django.db import models

class User(models.Model):
    name=models.CharField(max_length=30,unique=True)
    active=models.BooleanField(default=True)
    password=models.CharField(max_length=500)
    # phone=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
