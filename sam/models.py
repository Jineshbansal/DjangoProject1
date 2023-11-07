from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()

class mockinterview(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='person2persons',to_field="email")
    domain = models.CharField(max_length=100)
    alum_id=models.ForeignKey(User, on_delete=models.CASCADE,related_name='friends')
    
    timing=models.DateTimeField()
    def save(self, *args, **kwargs):
        if self.alum_id.alumni:
            if not self.student_id.alumni:
                raise ValueError("Data can only be saved when student is also an alumni")
        else:
            raise ValueError("Data can only be saved when alum_id is an alumni")
        super(mockinterview, self).save(*args, **kwargs)



class avf(models.Model):
    courses = models.CharField(max_length=100)
    branch= models.CharField(max_length=100)  
    alum_id=models.ForeignKey(User, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if self.alum_id.alumni:
            super(avf, self).save(*args, **kwargs)
        else:
            raise ValueError("Data can only be saved when staff is True")
        



class sam(models.Model):

    location = models.CharField(max_length=100)
    Schedule=models.DateTimeField()
    alum_id=models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    def save(self, *args, **kwargs):
        if self.alum_id.alumni:
            super(sam, self).save(*args, **kwargs)
        else:
            raise ValueError("Data can only be saved when staff is True")
        

