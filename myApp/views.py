from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        if User.objects.filter(
            username = request.POST['username'],
            password = request.POST['password']
        ).exists():
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')
            


def apointment(request):
    return render(request, 'apointment.html')

def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def doctors(request):
    return render(request, 'doctors.html')


#register user view

def register(request):
    if request.method == 'POST':
        members = User(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
            
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')
        

def login(request):
    return render(request, 'login.html')