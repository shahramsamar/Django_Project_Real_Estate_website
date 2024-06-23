from django.shortcuts import render, redirect
from website.forms import NewsletterForm, ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse


def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

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
    context ={'form':form}   
    return render(request, 'website/contact.html',context)



def property_view(request):
    return render(request, 'website/property.html')



def newsletter_view(request):
    if request.method =="POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
    