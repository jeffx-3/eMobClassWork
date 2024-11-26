import json
import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from django.shortcuts import render,redirect

from myApp.credentials import LipanaMpesaPpassword, MpesaAccessToken
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


###Mpesa API

def token(request):
    consumer_key = 'mKuvmK7mCV6hi9r2gFLnZFowGOaAUpOAbpFpsrUMA3tuavb9'
    consumer_secret = 'PVjxCjFYzmNUtfNO5bVYzJYgROWcKjdurDlg4p5vDmAhv3AFA2KHhq6L5KPotbPF'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")