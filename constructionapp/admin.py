from django.contrib import admin
from .models import  SliderHome, About, Services, Preview_Images, ServiceType, SubServiceslist, Features, Clients, Contact, ContactMessage, Team, Testimonials, Portfolio, PortFolioImage, PortfolioStatus 
# Register your models here.

admin.site.register(SliderHome)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Preview_Images)
admin.site.register(ServiceType)
admin.site.register(SubServiceslist)
admin.site.register(Features)
admin.site.register(Clients)
admin.site.register(Contact)
admin.site.register(ContactMessage)
admin.site.register(Team)
admin.site.register(Testimonials)
admin.site.register(Portfolio)
admin.site.register(PortFolioImage)
admin.site.register(PortfolioStatus)


# admin.site.register(ProjectStatus)
# admin.site.register([SliderHome, About, Services, Preview_Images, ServiceType, Team, Testimonials])
