from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from blog.forms import NewsletterForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post_time(request):
    date_time = timezone.now()
    post = Post.objects.filter(status=1, published_date__lte=date_time)
    return post

def blog_view(request, **kwargs):
    posts = post_time(request)
    
    if kwargs.get('cat_name')!=None:
        posts = posts.filter(category__name=kwargs['cat_name'])
        
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username']) 
          
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])  
        
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page") 
        posts = posts.page(page_number)
        
    except PageNotAnInteger:   
         posts = posts.get_page(1)
    
    except EmptyPage:
         posts = posts.get_page(1)

        
    context = {"posts":posts}
    return render(request,'blog/blog_home.html', context)



def blog_single(request, pid):
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,"Your comment submited successfully")
        else:
            messages.add_message(request,messages.ERROR,"Your comment Failed successfully") 
             
    date_time = timezone.now()
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=date_time)
    post.counted_views += 1
    post.save()
    
             
    # related_post = Post.objects.filter(status=1,published_date__lte=date_time)
    comments = Comment.objects.filter(post=post.id, approved=True)
    form = CommentForm()
    context ={"post":post,'comments': comments, 'form':form }
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
        if search :=request.GET.get("search"):
            posts = posts.filter(content__contains=search)
    context ={"posts":posts}  
    return render (request,'blog/blog_home.html', context)      


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog_home.html', context)
    
    