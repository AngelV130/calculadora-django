from django.shortcuts import render, get_object_or_404

def home_page(request, *args, **kwargs):
    title = "Welcome home"
    context = {
        "title": title,
    }
    return render(request, "pages/home.html", context)

def calculadora_page(request, *args, **kwargs):
    title = "Welcome home"
    context = {
        "title": title,
    }
    return render(request, "pages/calculadora.html", context)