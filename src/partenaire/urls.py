
from django.urls import re_path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
   re_path(r'^$',
       TemplateView.as_view(template_name='partenaire/partenaire_list.html'),
       name='partenaire_list'),
]
