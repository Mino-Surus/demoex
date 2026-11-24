from django.db import models
from django.contrib.auth.models import User
# from django.conf import settings

# User = settings['AUTH_USER_MODEL']

class Doctor (models.Model): 
    full_name = models.CharField(max_length=100)
    
    
class Service(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=[
        ('new', 'Новая'),
        ('confirmed', 'Подтверждено'),
        ('complited', 'Завершено'),
    ], default='new')
    
class Comment(models.Model):
    title = models.CharField()
    text = models.TextField(max_length=10000)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    