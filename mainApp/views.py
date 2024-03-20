from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
def blog(request):
    return render(request, 'blog.html')
