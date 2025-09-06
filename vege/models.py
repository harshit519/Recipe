from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class rcp(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    rcp_name=models.CharField(max_length=100)
    rcp_description=models.TextField()
    rcp_image=models.ImageField(upload_to='receiptes')


    def __str__(self) -> str:
        return  self.rcp_name
        

