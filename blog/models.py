from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.name 
    
class Post(models.Model):
    image = models.ImageField(upload_to='blog_image/',default='')
    title = models.CharField(max_length=255)
    content = HTMLField()       
    tags = TaggableManager()
    Category =models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_required = models.BooleanField(default=False)
    
    
    class Meta:
        ordering =['-created_date'] 
    
    def __str__(self):
        return f"{self.title}  - {self.id}"
    
    def get_absolute_url(self):
        return reverse("blog:blog_single", kwargs={"pid": self.id})
    