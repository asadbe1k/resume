from django.shortcuts import render, redirect
from .models import Message

# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get("fullname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if all([name, email, message]):
            Message.objects.create(
                name=name,
                email=email,
                message=message,
            )
            return redirect(home)
    return render(request, "index.html")
