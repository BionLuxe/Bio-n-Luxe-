from django.shortcuts import render

from mainApp.models import *
from django.contrib import messages
def index(request):
    slides = Slide.objects.all()
    services = Services.objects.all()
    about = About.objects.first() 
    testimonials = Testimonial.objects.all() 
    blog_posts = BlogPost.objects.all()
    context = {'slides': slides, 
               'about': about,
               'services': services,
               'testimonials': testimonials,
               'blog_posts': blog_posts
               }
    return render(request, 'index.html', context)


def aboutus(request):
    about = About.objects.first() 
    staff = Team.objects.all() 
    context = {
               'about': about,
               'services': services,
               'staff': staff
               }

    return render(request, 'about.html',context)

def contact(request):
    about = About.objects.first() 
    context = {
        'about': about,
        'services': services
               
        }

    return render(request, 'contact.html',context)

def services(request):
    services = Services.objects.all()
    about = About.objects.first() 
    context = {
        'about': about,
        'services': services
               
        }
    return render(request, 'services.html',context)

def blog(request):
    about = About.objects.first() 
    blog_posts = BlogPost.objects.all()

    context = {
        'about': about,
        'blog_posts': blog_posts,
               
        }

    return render(request, 'blog.html',context)
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            subscriber = Subscriber.objects.create(email=email)
            messages.success(request, 'Thank you for subscribing!')
        except Exception as e:
            messages.error(request, 'Error occurred while subscribing. Please try again later.')

    return render(request, 'subscribe.html')


def policy(request):
    return render(request, 'policies.html')