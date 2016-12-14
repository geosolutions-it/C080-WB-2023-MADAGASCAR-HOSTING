<<<<<<< HEAD
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views



urlpatterns = patterns('partenaire.views',
   url(r'^$',
       TemplateView.as_view(template_name='partenaire/partenaire_list.html'),
       name='partenaire_list'),
    )

=======
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
>>>>>>> 9c269c01542befb8fbb9791076aa2b98dd31892e
