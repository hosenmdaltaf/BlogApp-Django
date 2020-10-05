from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200,null= True)
    image=models.ImageField(upload_to='img', null=True,blank=True,default='/static/images/cover.jpg')
    date=models.DateTimeField(auto_now_add=True)
    details=models.TextField()


    def __str__(self):
        return self.title

  
