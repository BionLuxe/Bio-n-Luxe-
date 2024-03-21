from django.shortcuts import render

from mainApp.models import *

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
