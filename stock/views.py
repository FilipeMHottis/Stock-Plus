from core.models import Product, Tag, Category
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            return redirect("products")
        else:
            return render(
                request,
                "login.html",
                {"error": "Invalid credentials"},
            )


def products(request):
    products = Product.objects.all()
    user = User.objects.get(username="admin")
    return render(
        request,
        "products.html",
        {
            "products": products,
            "user": user,
        },
    )


def product_create(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()

    return render(
        request,
        "product_create.html",
        {
            "tags": tags,
            "categories": categories,
        },
    )


def tag_create(request):
    return render(request, "tag_create.html")


def category_create(request):
    return render(request, "category_create.html")
