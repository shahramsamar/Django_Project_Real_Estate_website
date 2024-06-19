from django import forms 
from blog.models import Newsletter, Comment




class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    model = Comment
    fields = ['post','name','email','subject','message']        
        
        