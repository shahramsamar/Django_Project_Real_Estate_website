from django import template
from django.utils import timezone
from blog.models import Category,Post


register = template.Library()




@register.inclusion_tag('blog/blog_post_category.html')
def post_category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}  
 

