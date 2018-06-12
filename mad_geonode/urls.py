from django.conf.urls import url, include
from django.views.generic import TemplateView
from partenaire.api import PartenaireResource

part_res= PartenaireResource()

from geonode.urls import urlpatterns

urlpatterns += [
## include your urls here
    url(r'^partenaire/', include('partenaire.urls')),
]

urlpatterns = [
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
] + urlpatterns
