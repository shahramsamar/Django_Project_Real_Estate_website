from django.shortcuts import render

# Create your views here.

def blog_view(request):
    return render(request,'blog/blog.html')



def blog_single_view(request):
    return render(request, 'blog/blog_single.html')