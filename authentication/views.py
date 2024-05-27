from django.shortcuts import render
from django.contrib.auth.models import User


def login(request):
    messages = []

    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)

            if user.check_password(password):
                messages.append("Login successful")
            else:
                messages.append("Incorrect password")

        except User.DoesNotExist:
            messages.append("User does not exist")

        return render(request, "login.html", {"messages": messages})
