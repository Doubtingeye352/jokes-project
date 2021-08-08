from django.shortcuts import redirect, render
from .models import pic
from datetime import date
from joke.jokes import *
import random
# Create your views here.

def home(request):
    pics = pic.objects
    var = random.choice([icanhazdad(),geek(),icndb()])
    return render(request,'home.html', {'pics': pics, 'var': var})

def upload(request):
    return render(request,'upload.html')

def done(request):
     if request.method == 'POST':
         if request.POST['title'] and request.FILES['image']:
             today = date.today()
             pi = pic()
             pi.name = request.POST['title']
             pi.picture = request.FILES['image']
             pi.date = today.strftime("%d/%m/%Y")
             pi.save()
             return redirect('home')
                         
         else:
            return render(request,'done.html')