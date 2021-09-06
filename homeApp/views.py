from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        ##If user is not logged in then render him the login page
        return redirect('/login')
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)

        #CHECK IF USER HAS ENTERED CORRECT CREDENTIALS
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
         # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    #if logout then return the login page
    return redirect('/login')