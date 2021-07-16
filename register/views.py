from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm
    return render(request, "registration/register.html", {"form" : form})

def profile_view(request):
    user = User.objects.get(username = request.user)
    return render(request, "profile.html", {"user" : user})
