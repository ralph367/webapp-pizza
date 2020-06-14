from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """
    Registration page 

    Args:
        request : user request

    Returns:
        redirect: 
            - if valid >> home page
            - if not valied >> show error in registration page
            - if GET request >> registration page 

    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = UserCreationForm()
    return render(request,"registration/register.html", {"form": form})