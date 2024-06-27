from django import template
from django.utils import timezone
from blog.models import Category, Post, Comment


register = template.Library()







@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts



@register.simple_tag(name='counted_comments')
def function(pid):
    post = Post.objects.filter(pk=pid)
    return Comment.objects.filter(post=pid, approved=True).count()



@register.inclusion_tag('blog/blog_popular_post_widget.html')
def popular_post_widget():
    posts = Post.objects.filter(status=1).order_by("published_date")[:3]
    return {"posts":posts}


@register.inclusion_tag('blog/blog_post_category.html')
def blog_post_category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}  
 
