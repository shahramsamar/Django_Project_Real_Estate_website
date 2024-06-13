from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from django.http import HttpResponseRedirect
from blog.forms import NewsletterForm

# Create your views here.

def blog_view(request, **kwargs):
    date_time = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=date_time)
    
    context = {"posts":posts}
    return render(request,'blog/blog_home.html', context)



def single(request, pid):
    date_time = timezone.now()
    post = get_object_or_404(Post, status=1, id=pid, published_date__lte=date_time)
    context ={"post":post}
    # related_post = Post.objects.filter(status=1,published_date__lte=date_time)
    # post_single.counted_views += 1
    # post_single.save()
    return render(request, 'blog/blog_single.html', context)

def test(request):
    date_time = timezone.now()
    post = get_object_or_404(Post,status=1, published_date__lte=date_time)
    context ={"post":post}
    return render(request,'blog/test.html', context)

def newsletter_view(request):
    if request.method =="POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = NewsletterForm()
    return render(request, 'blog/newsletter.html', {'form': form})