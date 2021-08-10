from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from django.conf import settings
from constructionapp.views import send_mail_all
from constructionapp.models import(
    SliderHome,
    About,
    Services,
    ServiceType,
    SubServiceslist,
    Preview_Images,
    Features,
    Team,
    Clients,
    Contact,
    ContactMessage,
    Portfolio,
    PortFolioImage,
    Testimonials,

)

from .serializer import(
    SliderHomeSerializer,
    AboutSerializer,
    ServiceTypeSerializer,
    ServicesSerializer,
    ServiceImageSerializer,
    SublistSerializer,
    FeaturesSerializer,
    TeamSerializer,
    ClientsSerializer,
    ContactSerializer,
    ContactMessageSerializer,
    PortfolioSerializer,
    PortFolioImageSerializer,
    TestimonialsSerializer,

)


@api_view(['GET'])
def api_list(request):
    
    objs = {
        'carousel':'/api/carousel',
        'about':'/api/about',
        'features':'/api/features',
        'services':'/api/services',
        'team':'/api/team',
        'our_clients':'/api/our_clients',
        'contact_info':'/api/contact_info',
        'contactmessage':'/api/contactmessage',
        'portfolio':'/api/portfolio',
        'testimonails':'/api/testimonials',

    }
    
    return Response(objs)

@api_view(['GET'])
def carousel(request):
    carousel = SliderHome.objects.all()
    serializer = SliderHomeSerializer(carousel, many=True)
    # carousel_list = serializer.data

    # objs ={
    #     'carousel':carousel_list,
    # }

    return Response(serializer.data)


@api_view(['GET'])
def about(request):
    about_infos = About.objects.all().last()
    serializer = AboutSerializer(about_infos, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def servicetype(request):
    servicetype = ServiceType.objects.all()
    serializer = ServiceTypeSerializer(servicetype, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def services(request):
    our_services = Services.objects.all()
    serializer = ServicesSerializer(our_services, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def sublist(request):
    sublist = SubServiceslist.objects.all()
    serializer = SublistSerializer(sublist, many=True)
   
    return Response(serializer.data)

@api_view(['GET'])
def previewimages(request):
    images = Preview_Images.objects.all()
    serializer = ServiceImageSerializer(images, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def features(request):
    feature = Features.objects.all()
    serializer = FeaturesSerializer(feature, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def teams(request):
    team = Team.objects.all()
    serializer = TeamSerializer(team, many=True)
   
    return Response(serializer.data)

@api_view(['GET'])
def ourclients(request):
    clients = Clients.objects.all()
    serializer = ClientsSerializer(clients, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def contactinfo(request):
    contact = Contact.objects.all().first()
    serializer = ContactSerializer(contact, many=False)
   
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def contact_list(request):
    
    if request.method == 'GET':
        contactmessage = ContactMessage.objects.all()
        serializer = ContactMessageSerializer(contactmessage, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            firstname = request.POST.get('firstname', '')
            lastname = request.POST.get('lastname', '')
            email =  request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            message = request.POST.get('message', '') 
            context = {'firstname': firstname, 'lastname': lastname, 'email': email, 'phone':phone, 'message':message}
            send_mail_all(context, email)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def portfolio(request):
    portfolio = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolio, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def portfolioimage(reqiuest):
    portfolioimage = PortFolioImage.objects.all()
    serializer = PortFolioImageSerializer(portfolioimage, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def testimonials(request):
    testimonials = Testimonials.objects.all()
    serializer = TestimonialsSerializer(testimonials, many=True)
  
    return Response(serializer.data)








