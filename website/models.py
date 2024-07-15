from django.db import models
from taggit.managers import TaggableManager
from tinymce.models import HTMLField



# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    
 
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering =['-created_date']
    
    def __str__(self) -> str:
        return super().__str__()        
        
class Property(models.Model):
    image = models.ImageField(upload_to='blog_image/',default='post_image/post.jpeg')
    title = models.CharField(max_length=255)
    content = HTMLField()       
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_user_required = models.BooleanField(default=False)   