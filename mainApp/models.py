from django.db import models
from django_summernote.fields import SummernoteTextField
class Slide(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slides/')
    slide_image = models.ImageField(upload_to='slides/', default='')
    caption = models.TextField()

    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/')
    description = SummernoteTextField()

    def __str__(self):
        return self.title
class Services(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')
    description = SummernoteTextField()

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='testimonials/')
    message = models.TextField()

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    content = SummernoteTextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Team(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.title