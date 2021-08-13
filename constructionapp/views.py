from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from rest_framework import generics
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from django.views import View
from django.forms.models import modelformset_factory
from django.template import RequestContext
import os

from django.contrib.auth.decorators import login_required
from .forms import (
    SubServicesForm,
    TestimonialForm,
    TestimonialUpdateForm,
    SliderHomeForm,
    AboutForm,
    ServicesForm,
    ServicesUpdateForm,
    ServiceTypeForm,
    PortFolioForm,
    FeaturesForm,
    TeamForm,
    ClientsForm,
    ContactForm,
    ContactMessageForm,
    PortFolioForm,
    PortFolioUpdateForm,

  
)

# for sending data to the admin mail address
def send_mail_all(context, email):
    content = {"%s: %s" % (key, value) for (key, value) in context.items()}
    content = "\n".join(content)

    send_mail(
        'Contact Message',  # subject
        content,  # message
        settings.EMAIL_HOST_USER,  # from email
        ['arjunkhattri83@gmail.com'],
        fail_silently=False)

@login_required
def dashboard(request):
    business_title = SliderHome.objects.all()
    context = {'business_title': business_title}
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def testimonials_list(request):
    review_list = Testimonials.objects.all()
    context = {'review_list':review_list}
    return render(request, 'testimonials/list.html', context)
    
@login_required
def create_testimonials(request):
    create_review =  Testimonials.objects.all()
    if request.method == 'POST':
        form = TestimonialForm(request.POST or None, request.FILES)
        try:
            if form.is_valid():
                form.save()
                messages.success(request,('New Testimonail created! '))
                return redirect('testimonials_list')
            else:
                messages.error(request, 'Invalid Testimonial details')
                return redirect('create_testimonials')
        except:
            if Testimonials.objects.filter(author__iexact = form.cleaned_data['author']).exists():
                messages.error(request, 'Testimonial already exists')
                return redirect('testimonails_list')
    else:
        context = {'create_review': create_review}
        return render(request, 'testimonials/create.html', context)

@login_required
def testimonials_details(request, name):
    review_details = Testimonials.objects.get(author=name)
    context = {'review_details': review_details }
    return render(request, 'testimonials/detail.html',context)


@login_required
def update_testimonials(request, name):
    review_update = Testimonials.objects.get(author=name)
    if request.method == 'POST':
        form = TestimonialUpdateForm(request.POST or None, request.FILES, instance=review_update)
        try:
            if form.is_valid():
                 review_update.save()
            else:
                review_update.quote = request.POST.get('quote')
                review_update.save()
            messages.success(request, "Testimonials Updated")
            return redirect('testimonials_list')
        except:
            messages.error(request, "Unable to update testimonial")
            return redirect('testimonials_list')

    elif request.method == 'GET':
        context={'review_update': review_update}
        return render(request, 'testimonials/update.html', context)


@login_required
def delete_testimonials(request, author):
    testimonials = Testimonials.objects.get(author=author)
    testimonials.delete()
    messages.success(request, "Testimonials Deleted!")
    return redirect('testimonials_list')


@login_required
def carousel_list(request):
    carousel= SliderHome.objects.all()
    context = {'carousel': carousel}
    return render(request, 'page/carousel/list.html', context)




@login_required
def carousel_create(request):
    if request.method == "POST":
        form = SliderHomeForm(request.POST or None, request.FILES)
        try:
            if form.save():
                form.save()
                messages.success(request, 'HomeSlider details added')
                return redirect('carousel_list')
            else:
                messages.error(request, 'Invalid home details entered')
                return redirect('carousel_list')
        except:
            return redirect('carousel_list')
    else:
        return render(request, 'page/carousel/create.html') 

@login_required
def carousel_detail(request, name):  
    carouseldetail = SliderHome.objects.get(title=name)
    context = {'carouseldetail':carouseldetail}
    return render(request, 'page/carousel/detail.html', context)

@login_required
def carousel_update(request, name):
    carouselupdate = SliderHome.objects.get(title=name) 
    if request.method=='POST':
        form = SliderHomeForm(request.POST or None, request.FILES, instance=carouselupdate)
        if form.is_valid():
            form.save()
            messages.success(request, 'carousel information updated!')
            return redirect('carousel_list')
        else:
            messages.error(request, 'Invalid home information!')
            return redirect('carousel_list')
    else:
        context = {'carouselupdate': carouselupdate}
        return render (request, 'page/carousel/update.html', context)


@login_required
def carousel_delete(request, id):
	context ={}
	obj = get_object_or_404(SliderHome, id = id)
	if request.method =="POST":
		obj.delete()

		return redirect('carousel_list')

	return render (request, 'page/carousel/delete.html', context)

@login_required
def about_info(request):
    info = About.objects.all().first()
    context = {'info': info}
    return render(request, 'page/about/view.html', context)

@login_required
def about_create(request):
    if request.method == 'POST':
        form = AboutForm(request.POST or None, request.FILES)
        try:
            if form.save():
                form.save()
                messages.success(request, 'About Details Added')
                return redirect('about_info')
            else:
                messages.error(request, 'Invalid About Details Entered!!')
                return redirect('about_info')
        except:
            return redirect('about_info')
    else:
        return render(request, 'page/about/create.html')

@login_required
def about_update(request):
    info = About.objects.all().last()
    if request.method == 'POST':
        form = AboutForm(request.POST or None, request.FILES, instance = info)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'About Details Updated')
                return redirect('about_info')
            else:
                messages.error(request, 'Invalid About Details Entered')
                return redirect('about_info')
        except:
            return redirect('about_info')
    else:
        context = {'info': info}
        return render(request,'page/about/update.html', context)


# @login_required
# def service_type(request):
#     subtype = ServiceType.objects.all()
#     context = {'subtype': subtype}
#     return render(request, 'page/services/subtype/list.html', context)

@login_required
def create_servicetype_list(request):
    subtype = ServiceType.objects.all()
    context = {'subtype': subtype}
    if request.method == 'POST':
        form = ServiceTypeForm(request.POST or None, request.FILES)
        try:
            if form.save():
                form.save()
                messages.success(request, 'Service type added')
                return redirect('create_servicetype')

            else:
                messages.error(request, 'Invalid Service Type Entered!')
                return redirect('create_servicetype')
        except:
            return redirect('create_servicetype')
    else:
        return render(request, 'page/services/subtype/create.html', context)

@login_required
def delete_servicetype(request, id):
	context ={}
	obj = get_object_or_404(ServiceType, id = id)
	if request.method =="POST":
		obj.delete()

		return redirect('create_servicetype')

	return render (request, 'page/services/subtype/delete.html', context)

@login_required
def services_list(request):
    subservices= SubServiceslist.objects.all()
    context = {'subservices':subservices}
    services = Services.objects.all()
    context = {'subservices': subservices, 'services': services}
    return render(request, 'page/services/list.html', context)


# class ServiceListView(ListView):
#     model = Services
#     template_name = 'page/services/list.html'
#     context_object_name = 'services'
    

class ServicesCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ServicesForm()
        return render(request, 'page/services/create.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ServicesForm(request.POST or None, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()

                for item in request.FILES.getlist('images'):
                    longthumb = Preview_Images.objects.create(longthumb=item, service=post)
                    longthumb.save()
                
                return redirect('services_list')
            else:
                messages.error(request, 'Invalid Services Details Entered')
                return redirect('services_list')
        else:
            return render(request, 'page/services/create.html')


class ServiceDetailView(DetailView):
    model = Services
    form_class = ServicesForm
    template_name = 'page/services/detail.html'


class ServiceUpdateView(UpdateView):
    model = Services
    form_class = ServicesUpdateForm
    template_name = 'page/services/update.html'

    def post(self, request, *args, **kwargs):
        services_qs = Services.objects.filter(pk=kwargs['pk'])
        
        if services_qs.exists():
            services = services_qs.first()
            form = self.form_class(request.POST or None, instance=services)
            if form.is_valid():
                post = form.save(commit=False)
                post.shortthumb = request.FILES.get('shortthumb')
                post.save()
                 

                if len(request.FILES.getlist('images'))>0:
                    longthumb = Preview_Images.objects.filter(service=post)
                    if longthumb.exists():
                        for images in longthumb:
                            images.delete()
                        for item in request.FILES.getlist('images'):
                            images = Preview_Images.objects.create(longthumb=item, service=post)
                            images.save()
                    else:
                        for item in request.FILES.getlist('images'):
                            images = Preview_Images.objects.create(longthumb=item, service=post)
                            images.save()
                            
                return redirect('services_list')
                
            else:
               return redirect('update_services', pk=kwargs['pk'])
        else:
            return render(request, 'page/services/update.html', {"services_qs":services_qs})

class ServiceDeleteView(DeleteView):
    model = Services
    success_url = reverse_lazy('services_list')
    template_name = 'page/services/delete.html'

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
                 
        
# @login_required
# def subservices_list(request):
#     subservices= SubServiceslist.objects.all()
#     context = {'subservices':subservices}
#     return render(request, 'page/services/subservices/list.html', context)

@login_required
def subservices_detail(request, name):  
    subservices = SubServiceslist.objects.filter(servicetitle=name)
    if subservices.exists():
        subservice =subservices.first()
    context = {'subservices':subservice}
    return render(request, 'page/services/subservices/detail.html', context)

# @login_required
# def create_subservices(request):
#     if request.method == 'POST':
#         form = SubServicesForm(request.POST or None, request.FILES)
#         try:
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Subservices Details Added')
#                 return redirect('services_list')
#             else:
#                 messages.error(request, 'Invalid Subservices Details Entered')
#                 return render ('services_list')
#         except:
#             return redirect('services_list')
    
#     elif request.method == 'GET':
#         form = SubServicesForm()
#         context = { 'form':form}
    
#         return render(request, 'page/services/subservices/create.html', context)

class SubServicesCreateView(View):

    def get(self, request, *args, **kwargs):
        form = SubServicesForm()
        return render(request, 'page/services/subservices/create.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SubServicesForm(request.POST or None, request.FILES)
            if form.is_valid():
                # post = form.save(commit=False)
                form.save()
                
                return redirect('services_list')
            else:
                messages.error(request, 'Invalid SubServices Details Entered')
                return redirect('services_list')
        else:
            return render(request, 'page/services/subservices/create.html')

# @login_required
# def update_subservices(request, pk):
    
#     subservices = SubServiceslist.objects.filter(id=pk)
 
#     s = subservices.first()
#     if request.method == 'POST':
#         form = SubServicesForm(request.POST or None, request.FILES, instance=s)
#         try:
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Subservices Details Updated!')
#                 return redirect('services_list')
#             else:
#                 messages.error(request, 'Invalid Subservice Details')
#                 return render('services_list')
#         except:
#             return redirect('services_list')
#     elif request.method == 'GET':
#         form = SubServicesForm()
#         context = {'form':form}
#         return render(request, 'page/services/subservices/update.html', context)

class SubServiceUpdateView(UpdateView):
    model = SubServiceslist
    form_class = SubServicesForm
    template_name = 'page/services/subservices/update.html'

    def post(self, request, *args, **kwargs):
        qs = SubServiceslist.objects.filter(pk=kwargs['pk'])
        
        if qs.exists():
            subservices = qs.first()
            form = self.form_class(request.POST or None, instance=subservices)
            if form.is_valid():
                # post = form.save(commit=False)
                # post.shortthumb = request.FILES.get('shortthumb')
                form.save()            
                            
                return redirect('services_list')
                
            else:
               return redirect('update_subservices', pk=kwargs['pk'])
        else:
            return render(request, 'page/services/subservices/update.html', {'qs':qs})


@login_required
def delete_subservices(request, id):
	context ={}
	obj = get_object_or_404(SubServiceslist, id = id)
	if request.method =="POST":
		obj.delete()

		return redirect('services_list')

	return render (request, 'page/services/subtype/delete.html', context)

@login_required
def portfolio_list(request):
    portfoliolist = Portfolio.objects.all()
    context = {'portfoliolist': portfoliolist}
    return render(request, 'page/portfolio/list.html', context)


class PortfolioView(CreateView):

    def get(self, request, *args, **kwargs):
        form = PortFolioForm()
        return render(request, 'page/portfolio/create.html', {'form':form})

    def post(self, request, *args, **kwargs):   
        if request.method == 'POST':
            form = PortFolioForm(request.POST or None, request.FILES)
            if form.is_valid():
                post = Portfolio.objects.create(title=request.POST.get('title'), 
                                                status=form.cleaned_data.get('status'), 
                                                description=request.POST.get('description'),
                                                )
                post.save()
              
                for item in request.FILES.getlist('images'):
                    image =  PortFolioImage.objects.create(image=item, portfolio=post)
                    image.save()     
                return redirect('portfolio_list')
                
            else:
                messages.error(request, 'Invalid portfolio information!')
                return redirect('portfolio_list')
            
        else:
            return render(self.request, 'page/portfolio/create.html')
            
class PortfolioDetail(DetailView):
    model = Portfolio
    template_name = 'page/portfolio/detail.html'



class PortfolioUpdateView(UpdateView):
    model = Portfolio
    form_class = PortFolioUpdateForm
    template_name ='page/portfolio/update.html'

    def post(self, request, *args, **kwargs):
        portfolio_qs = Portfolio.objects.filter(pk=kwargs['pk'])
        if portfolio_qs.exists():
            portfolio = portfolio_qs.first()
            form = self.form_class(request.POST or None, instance=portfolio)
            if  form.is_valid():
                post = form.save(commit=False)
                post.save()
                if len(request.FILES.getlist('images'))>0:
                    images = PortFolioImage.objects.filter(portfolio=post)
                    if images.exists():
                        for image in images:
                            image.delete()
                        for item in request.FILES.getlist('images'):
                            image = PortFolioImage.objects.create(image=item, portfolio=post)
                            image.save()
                    else:
                        for item in request.FILES.getlist('images'):
                            image = PortFolioImage.objects.create(image=item, portfilio=post)
                            image.save()
                
                return redirect('portfolio_list')
            else:
                return redirect('update_portfolio', pk=kwargs['pk'])
            # return redirect('portfolio_list')
        else:
            return redirect('portfolio_list')


class PortfolioDeleteView(DeleteView):
    model = Portfolio
    success_url = reverse_lazy('portfolio_list')
    template_name = 'page/portfolio/delete.html'

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
                 
    




@login_required
def features_list(request):
    feature = Features.objects.all()
    context = {'feature':feature}
    return render(request, 'page/features/list.html', context)

@login_required
def create_features(request):
    if request.method == 'POST':
        form = FeaturesForm(request.POST or None, request.FILES)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Features Added')
                return redirect('features_list')
            else:
                messages.error(request, 'Failed to add the feature!')
                return redirect('features_list')
        except:
            return redirect('features_list')
    else:
        return render(request, 'page/features/create.html')

@login_required
def feature_detail(request, name):
    feature = Features.objects.get(title=name)
    context = {'feature': feature}
    return render(request, 'page/features/details.html', context)

@login_required
def update_features(request, name):
    feature = Features.objects.get(title=name)
    if request.method == 'POST':
        form = FeaturesForm(request.POST or None, request.FILES, instance=feature)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Feature updated succesfully')
                return redirect('features_list')
            else:
                messages.error(request, 'Failed to update features')
                return redirect('features_list')
        except:
            return redirect('features_list')
    else:
        context = {'feature':feature}
        return render(request, 'page/features/update.html', context)

@login_required
def features_delete(request, id):
	context ={}
	obj = get_object_or_404(Features, id = id)
	if request.method =="POST":
		obj.delete()

		return redirect('features_list')

	return render (request, 'page/features/delete.html', context)


@login_required
def team_list(request):
    teamlist = Team.objects.all()
    context = {'teamlist':teamlist}
    return render(request, 'page/team/list.html', context)

@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST or None, request.FILES)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Team Details Added Successfully')
                return redirect('team_list')
            else:
                messages.error(request, 'Failed to Add Team Details')
                return redirect('team_list')
        except:
            return redirect('team_list')
    else:
        return render(request, 'page/team/create.html')


@login_required
def team_detail(request, string):
    team = Team.objects.get(name=string)
    context = {'team': team}
    return render(request, 'page/team/details.html', context)

@login_required
def update_team(request, string):
    team = Team.objects.get(name=string)
    if request.method == 'POST':
        form = TeamForm(request.POST or None, request.FILES, instance = team)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Team Details Updated')
                return redirect('team_list')
            else:
                messages.error(request, 'Unable to Update Team Details')
                return redirect('team_list')
        except:
            return redirect('team_list')
    else:
        context = {'team': team}
        return render(request, 'page/team/update.html', context)

@login_required
def delete_team(request, id):
	context ={}
	obj = get_object_or_404(Team, id = id)
	if request.method =="POST":
		obj.delete()

		return redirect('team_list')

	return render (request, 'page/team/delete.html', context)

@login_required
def clients_list(request):
    clients = Clients.objects.all()
    context = {'clients': clients}
    return render(request, 'page/clients/list.html', context)

@login_required
def create_clients(request):
    if request.method == 'POST':
        form = ClientsForm(request.POST or None, request.FILES)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Client Added Successfully')
                return redirect('clients_list')
            else:
                messages.error(request, 'Failed to Add Client')
                return redirect('clients_list')
        except:
            return redirect('clients_list')
    else:
        return render(request, 'page/clients/create.html')

@login_required
def clients_detail(request, name):
    client = Clients.objects.get(clientname=name)
    context = {'client': client}
    return render(request, 'page/clients/details.html', context)

@login_required
def update_clients(request, name):
    client = Clients.objects.get(clientname=name)
    if request.method == 'POST':
        form = ClientsForm(request.POST or None, request.FILES, instance = client)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Client Details Updated Successfully')
                return redirect('clients_list')
            else:
                messages.error(request, 'Failed to Update Client Details')
                return redirect('clients_list')
        except:
            return redirect('clients_list')
    else:
        context = {'client' : client}
        return render(request, 'page/clients/update.html', context)

@login_required
def delete_clients(request, id):
	context ={}
	obj = get_object_or_404(Clients, id = id)
	if request.method =="POST":
		obj.delete()

		return redirect('clients_list')

	return render (request, 'page/clients/delete.html', context)


@login_required
def contact_list(request):
    contact = Contact.objects.all()
    context = {'contact':contact}
    return render(request, 'page/contact/list.html', context)

@login_required
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None, request.FILES)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Contact Details Created')
                return redirect('contact_list')
            else:
                messages.error(request, 'Unable to create contactform')
                return redirect('contact_list')
        except:
            return redirect('contact_list')
    else:
        return render(request, 'page/contact/create.html')

@login_required
def contact_details(request):
    # contact = Contact.objects.get(title=name)
    contact = Contact.objects.all().first()
    context = {'contact': contact}
    return render(request, 'page/contact/details.html', context)

@login_required
def update_contact(request):
    # contact = Contact.objects.get(title=name)
    contact = Contact.objects.all().first()
    if request.method == 'POST':
        form = ContactForm(request.POST or None, request.FILES, instance = contact)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Contact Details Updated')
                return redirect('contact_details')
            else:
                messages.error(request, 'Unable to update contactform')
                return redirect('contact_details')
        except:
            return redirect('contact_details ')
    else:
        context = {'contact':contact}
        return render(request, 'page/contact/update.html', context)



class ContactMessageList(ListView):
    model = ContactMessage
    template_name = 'page/contactmessage/list.html'
    context_object_name = 'message'


class ContactMessageDetail(DetailView):
    model = ContactMessage
    form_class = ContactMessageForm
    template_name = 'page/contactmessage/detail.html'
    context_object_name = 'messages'

class ContactMessageCreate(CreateView):
    
    def get(self, request, *args, **kwargs):
        form = ContactMessageForm()
        return render(request, 'page/contactmessage/create.html', {'form':form})

    def post(self, request, *args, **kwargs):   
        if request.method == 'POST':
            firstname = request.POST.get('firstname', '')
            lastname = request.POST.get('lastname', '')
            email =  request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            message = request.POST.get('message', '') 
            form = ContactMessageForm(firstname=firstname, lastname=lastname, emailaddress=email, phone=phone, message=message)
            form.save()
               
            context = {'firstname': firstname, 'lastname': lastname, 'email': email, 'phone':phone, 'message':message}

           
            send_mail_all(context, email)
            return render(request, 'page/contactmessage/create.html', context)


class ContactMessageDelete(DeleteView):
    model = ContactMessage
    success_url = reverse_lazy('contact_message')
    template_name = 'page/contactmessage/delete.html'