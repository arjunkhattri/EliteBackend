from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_list, name='api_list'),
    path('carousel/', views.carousel, name='carousel'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('services/', views.services, name='services'),
    path('services/servicetype', views.servicetype, name='servicetype'),
    path('services/previewimages/', views.previewimages, name='previewimages'),
    path('services/sublist/', views.sublist, name='sublist'),
    path('team/', views.teams, name = 'team'),
    path('our_clients', views.ourclients, name='our_clients'),
    path('contact_info', views.contactinfo, name = 'contact_info'),
    path('contactmessage', views.contact_list, name= 'contactmessage'),
    path('portfolio', views.portfolio, name = 'portfolio'),
    path('testimonials/', views.testimonials, name = 'testimonials'),
    
]

