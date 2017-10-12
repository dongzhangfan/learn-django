from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')  # Django automatically search folders called tempaltes
