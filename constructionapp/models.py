from typing import Reversible
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import  RichTextUploadingField
from django.contrib.auth.models import User
# Create your models here.

class SliderHome(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    text = RichTextUploadingField(blank=True, null=True)
    bg_image = models.ImageField(upload_to='media/Slider')

    def  __str__(self):
        return self.title
        
    def delete(self, *args, **kwargs):
        self.bg_image.delete()
        super().delete(*args, **kwargs)

    
class About(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, default= ' ')
    shortdesc = RichTextUploadingField(blank=True, null=True)
    short_thumb = models.ImageField(upload_to='media/about')
    longdesc = RichTextUploadingField(blank=True, null=True)
    long_thumb = models.ImageField(upload_to='media/about')

    def __str__(self):
        return self.title


class ServiceType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, default=' ' )
    image = models.ImageField(upload_to='media/subservices', blank=True)
    
    def __str__(self):
        return self.name
    

class Services(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True )
    shortdesc = RichTextUploadingField(blank=True, null=True)
    shortthumb = models.ImageField(upload_to='media/services')
    longdesc = RichTextUploadingField(blank=True, null=True)
    servicetype = models.ForeignKey(ServiceType, null=False, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("services_detail", kwargs={"pk": self.pk})
    
    @property
    def images(self):
        return self.images.all()
    
    @property
    def get_status(self):
        if len(self.images.all())> 0:
            return True
        else:
            return False
    
    
    def __str__(self):  
        return self.title
    


class SubServiceslist(models.Model):
    servicetitle = models.CharField(max_length=50, null=False, blank=False)
    description =RichTextUploadingField(blank=True, null=True)
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='subservices')
    
    def __str__(self):
        return self.servicetitle

class Preview_Images(models.Model):
    longthumb = models.ImageField(upload_to='media/services', blank=True, null=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.service.title

    def delete(self, *args, **kwargs):
        self.longthumb.delete()
        super().delete(*args, **kwargs)


class Features(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False, default='')
    description = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='media/features')

    def __str__(self):
        return self.title

class Clients(models.Model):
    clientname = models.CharField(max_length=254, null = True, blank = True)
    image = models.ImageField(upload_to='media/clients')
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.clientname


class Contact(models.Model):
    title = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=254, null=True, blank=True, default='')
    phone = models.CharField(max_length=100, null=True, blank = True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=254, null=True, blank=True)
    emailaddress = models.EmailField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=254, null=True, blank=True)
    message = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.firstname


class Team(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    designation = models.CharField(max_length=254, null=False, blank=False)
    profilepic = models.ImageField(upload_to='media/team')
    Bio = RichTextUploadingField(blank=True, null=True)
    address = models.CharField(max_length=254, null=False, blank=False)
    phone = models.FloatField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, unique=True)
    website = models.URLField(max_length=254, blank=True)

    def  __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.profilepic.delete()
        super().delete(*args, **kwargs)


class PortfolioStatus(models.Model):
    status_title = models.CharField(max_length=100, null=False, blank=True)
   
    def __str__(self):
        return self.status_title

class Portfolio(models.Model):
    STATUS_CHOICES=(
        ('Proposed', 'Proposed'),
        ('On Going', 'On Going'),
        ('Completed','Completed')

    )
    title = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=256, choices=STATUS_CHOICES, default='Proposed')
    description = RichTextUploadingField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={'pk': self.pk})

    @property
    def images(self):
        return self.images.all()

    @property
    def get_status(self):
        if len(self.images.all())> 0:
            return True
        else:
            return False
    
    def __str__(self):  
        return self.title


class PortFolioImage(models.Model):
    image = models.ImageField(upload_to='media/portfolio', null=False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.portfolio.title


class Testimonials(models.Model):
    author = models.CharField(max_length=50, null=False, blank=True)
    image = models.ImageField(upload_to='media/testimonialthumb')
    quote = models.TextField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.author 

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


    






