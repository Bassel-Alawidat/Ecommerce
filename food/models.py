from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Item(models.Model):           #this is like a table in mysql

    def __str__(self) -> str:
        return self.item_name
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default='https://cdn-icons-png.flaticon.com/512/2737/2737035.png')


    def get_absolute_url(self):
        return reverse('food:detail',kwargs={'pk':self.pk})