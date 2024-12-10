from django.shortcuts import render


def index(request):
    return render(request, 'myApp/main/index.html')  # This should match your folder structure
