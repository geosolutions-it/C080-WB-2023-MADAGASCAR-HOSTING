from django.conf.urls import patterns, url
from django.views.generic import TemplateView
<<<<<<< HEAD
from partenaire.api import PartenaireResource
from geonode.urls import *

part_res= PartenaireResource()

=======

from geonode.urls import *
>>>>>>> 9c269c01542befb8fbb9791076aa2b98dd31892e

urlpatterns = patterns('',
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
<<<<<<< HEAD
      (r'^partenaire/', include('partenaire.urls')),
      (r'^api/', include(part_res.urls)),

=======
   (r'^partenaire/', include('partenaire.urls')),
>>>>>>> 9c269c01542befb8fbb9791076aa2b98dd31892e

 ) + urlpatterns
