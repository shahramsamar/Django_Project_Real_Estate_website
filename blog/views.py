from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from django.http import HttpResponseRedirect
from blog.forms import NewsletterForm

# Create your views here.

def post_time(request):
    date_time = timezone.now()
    post = Post.objects.filter(status=1, published_date__lte=date_time)
    return post

def blog_view(request, **kwargs):
    posts = post_time(request)
    
    if kwargs.get('cat_name')!=None:
        posts = posts.filter(category__name=kwargs['cat_name'])
        
    context = {"posts":posts}
    return render(request,'blog/blog_home.html', context)



def blog_single(request, pid):
    date_time = timezone.now()
    post = get_object_or_404(Post,pk=pid,status=1,published_date__lte=date_time)
    
    # related_post = Post.objects.filter(status=1,published_date__lte=date_time)
    post.counted_views += 1
    post.save()
    context ={"post":post}
    return render(request, 'blog/blog_single.html', context)


def newsletter_view(request):
    if request.method =="POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = NewsletterForm()
    return render(request, 'blog/newsletter.html', {'form': form})

def blog_search(request):
    posts = post_time(request)
    if request.method =="GET":
        if var :=request.GET.get("search"):
            posts = posts.filter(content__contains=var)
    context ={"posts":posts}  
    return render (request,'blog/blog_home.html', context)      

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
    
    