from tastypie.resources import ModelResource
from partenaire.models import Partenaire
import time

class PartenaireResource(ModelResource):
    class Meta:
        queryset = Partenaire.objects.all()
        resource_name = 'partenaire'
        allowed_methods = ['get', 'post', 'put']
        