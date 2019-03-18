from django.shortcuts import render
from . models import Post
# Create your views here.

def home(request):

    context={
        'posts':Post.objects.all()
    }
    return render(request, 'new/home.html',context)


    
    
def about(request):
    return render(request, 'new/about.html')


    

def contact(request):
    return render(request, 'new/contact.html')


    
    