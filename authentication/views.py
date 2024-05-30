from django.shortcuts import render
from django.contrib.auth import authenticate


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            print("User is authenticated")
            return render(request, "login.html")
        else:
            return render(
                request,
                "login.html",
                {"error": "Invalid credentials"},
            )
