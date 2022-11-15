from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from myapp.forms import EmailLogin



# Create your views here.

def email_login(request):
    if "email" in request.session:
        return redirect("profile")
    if request.method == "GET":
        form = EmailLogin()
    else:
        form = EmailLogin(request.POST)
        if form.is_valid():
            request.session["email"] = form.cleaned_data["email"]
            request.session['full_name'] = form.cleaned_data["full_name"]
            request.session['age'] = form.cleaned_data["age"]
            request.session['gender'] = form.cleaned_data["gender"]
            return redirect("profile")
    return render(request, "myapp/login.html", {"form": form})

def profile(request):
    return render(request, "myapp/profile.html")

def logout(request):
    request.session.pop("email")
    request.session.pop("full_name")
    request.session.pop("gender")
    request.session.pop("age")

    return render(request,"myapp/login.html")


      
   
        
           
