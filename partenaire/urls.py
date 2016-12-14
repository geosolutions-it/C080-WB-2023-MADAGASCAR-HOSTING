from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views



urlpatterns = patterns('partenaire.views',
   url(r'^$',
       TemplateView.as_view(template_name='partenaire/partenaire_list.html'),
       name='partenaire_list'),
    )

