from django.db import models
from django.contrib.auth.models import User,AbstractUser
from .manager import UserManager

class User(AbstractUser):
    dept_choices=[
        ('CSE','CSE'),
        ('MNC','MNC'),
        ('ECE','ECE'),
        ('EEE','EEE'),
        ('MEC','MEC'),
        ('CER','CER'),
        ('CHE','CHE'),
        ('CIV','CIV'),
        ('MET','MET'),
        ('MIN','MIN'),
        ('PHE','PHE'),
        ('APD','APD'),
    ]
    sem_choices=[
        ('YES','YES'),
        ('NO','NO'),
        
    ]
    username=None
    email_token=models.CharField(max_length=200,null=True,blank=True)
    forget_password=models.CharField(max_length=200,null=True,blank=True)
    email= models.EmailField(unique=True)
    # user_profile_image = models.ImageField(upload_to="profile")
    department=models.CharField(max_length=20,choices=dept_choices,null=True)
    alumni=models.CharField(max_length=10,choices=sem_choices,null=True)
    objects=UserManager()
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS=[]
    


# Create your models here.
