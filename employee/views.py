from django.shortcuts import render


def home_view(request):
    return render(request, "employee/index.html")


def contact_view(request):
    return render(request, "employee/contact.html")
