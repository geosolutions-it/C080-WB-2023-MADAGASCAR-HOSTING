from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from partenaire.api import PartenaireResource
from geonode.urls import *

part_res= PartenaireResource()

from geonode.urls import *

urlpatterns = patterns('',
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
   (r'^partenaire/', include('partenaire.urls')),

 ) + urlpatterns
