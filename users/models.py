from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    #email = models.EmailField(unique=True)

    #USERNAME_FIELD: str = 'email'
    #REQUIRED_FIELDS = []
    pass
