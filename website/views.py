from django.shortcuts import render, redirect
from website.forms import NewsletterForm, ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse


def index_view(request):
    context = {'meta_description': 'A custom description for the home page.'}
    return render(request, 'website/index.html', context)

def about_view(request):
    context ={'meta_description': 'Learn more about us and what we do.'}
    return render(request, 'website/about.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # added selection by user 
        request.POST._mutable = True
        request.POST['name'] = 'Anonymous'
        if form.is_valid():
            form.save()
            # Add a success message
            messages.add_message(request,messages.SUCCESS,'your ticket Submited Successfully')
        else:
            # Add an error message
            messages.add_message(request, messages.ERROR,'your ticket did not Submited Successfully' )
    form = ContactForm()            
    context ={'form':form, 'meta_description': 'Learn more contact us and what we do.'}   
    return render(request, 'website/contact.html',context)



def property_view(request):
    return render(request, 'website/property.html')



def newsletter_view(request):
    if request.method =="POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'subscribe Successfully')
            return HttpResponseRedirect("/")
        else:
            messages.add_message(request, messages.ERROR,'subscribe UnSuccessfully' )
            return HttpResponseRedirect("/")
        
def custom_400(request, exception):
    return render(request, 'error/400.html', status=400)

def custom_403(request, exception):
    return render(request, 'eroor/403.html', status=403)

def custom_404(request, exception):
    return render(request, 'eroor/404.html', status=404)

def custom_500(request):
    return render(request, 'eroor/500.html', status=500)       
    