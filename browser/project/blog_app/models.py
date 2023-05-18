from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATUS=((0,"Draft"),(1,"Publishedd"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.FileField(upload_to="images/",max_length=400,null=True,default=None)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    class meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title    