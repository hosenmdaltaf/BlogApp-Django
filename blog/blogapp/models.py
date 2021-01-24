from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic',null=True,blank=True,default='/static/images/cover.jpg')
   
    def __str__(self):
        return str(self.author)

class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='img', null=True,blank=True,default='/static/images/cover.jpg')
    date=models.DateTimeField(default=timezone.now)
    details=models.TextField()
    author= models.ForeignKey('Author',on_delete=models.CASCADE)
    view_count=models.IntegerField(default=0,null=True,blank =True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blogapp:articale-detail', kwargs={'pk':self.pk})
    

  
