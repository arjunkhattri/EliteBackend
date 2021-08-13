from rest_framework import  serializers, fields
from constructionapp.models import (
    SliderHome,
    About,
    Features,
    Services,
    Preview_Images,
    ServiceType,
    SubServiceslist,
    Team,
    Clients,
    Contact,
    ContactMessage,
    Portfolio,
    PortFolioImage,
    # ProjectStatus,
    Testimonials

)


class SliderHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderHome
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'shortdesc', 'short_thumb', 'longdesc', 'long_thumb')

class ServiceImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Preview_Images
        # fields = '__all__'
        fields = ('id', 'longthumb')
        

class ServicesSerializer(serializers.ModelSerializer):
    images =  serializers.SerializerMethodField()
    sublist = serializers.SerializerMethodField()
    
    class Meta:
        model = Services
        # fields = '__all__'
        fields = ( 'id', 'title', 'shortdesc', 'shortthumb', 'longdesc', 'servicetype', 'images', 'sublist')

    def get_images(self, services):
        images = services.images.all()
        return ServiceImageSerializer(images, many=True).data

    def get_sublist(self, services):
        return SublistSerializer(services.subservices, many=True).data

    # def get_images(self, services):
    #     return ServiceImageSerializer(services.preview_images_set.all(), many=True).data

    # def get_sublist(self, services):
    #     return SublistSerializer(services.subserviceslist_set.all(), many=True).data


class SublistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubServiceslist
        # fields = '__all__'
        fields = ('description',)

class ServiceTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceType
        fields = '__all__'

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

# class ProjectStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectStatus
#         fields = ('title')


class PortFolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortFolioImage
        fields = ('image',)

class PortfolioSerializer(serializers.ModelSerializer):
    images =  serializers.SerializerMethodField()
    # status = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = ('title', 'date', 'status', 'description', 'images', 'status')

    def get_images(self, portfolio):
        images = PortFolioImage.objects.filter(portfolio=portfolio)
        # return PortFolioImageSerializer(portfolio.portfolioimage_set.all(), many=True).data
        return PortFolioImageSerializer(images, many=True).data

    # def get_status(self, portfolio):
    #     return ProjectStatusSerializer(portfolio.projectstatus_set.all(), many=True).data

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'



