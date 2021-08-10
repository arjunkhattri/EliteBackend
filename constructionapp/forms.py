from django import forms
from multiupload.fields import MultiImageField
from .models import(
    Preview_Images,
    Testimonials,
    SliderHome,
    About,
    Services,
    ServiceType,
    SubServiceslist,
    Clients,
    Portfolio,
    Features,
    Team,
    Contact,
    ContactMessage,

)
class TestimonialForm(forms.ModelForm):
    class Meta:
         model = Testimonials
         fields = '__all__'

class TestimonialUpdateForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = [
            'image',
            'quote',
        ]

class SliderHomeForm(forms.ModelForm):
    class Meta:
        model = SliderHome
        fields = [
            'title',
            'text',
            'bg_image',
        ]

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

class ServicesForm(forms.ModelForm):
    images=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    shortthumb= forms.ImageField()

    class Meta:
        model = Services
        fields = (
            'title',
            'shortdesc',    
            'shortthumb',
            'longdesc',
            'images',
            'servicetype',     
        )

class ServicesUpdateForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = (
            'title',
            'shortdesc',
            'shortthumb',
            'longdesc',
            'servicetype',
        )

 

class SubServicesForm(forms.ModelForm):
    class Meta:
        model = SubServiceslist
        fields = '__all__'

class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = '__all__'

class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'

class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = '__all__'



class PortFolioForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Portfolio
        fields = [
            'title',
            'status',
            'description',
            'images',
            
        ]


class PortFolioUpdateForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'title',
            'status',
            'description',
          
            
        ]
  

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'





