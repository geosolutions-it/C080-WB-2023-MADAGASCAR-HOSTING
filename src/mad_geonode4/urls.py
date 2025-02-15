# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import include
from django.urls import re_path
from django.views.generic import TemplateView

from geonode.urls import urlpatterns


from oca import HomePage
from partenaire.api import PartenaireResource

part_res= PartenaireResource()

'''
# You can register your own urlpatterns here
urlpatterns = [
    url(r'^/?$',
        homepage,
        name='home'),
 ] + urlpatterns
'''
urlpatterns += [
## include your urls here
    re_path(r'^partenaire/', include('partenaire.urls')),
]

urlpatterns = [
   # url(r'^/?$',
   #     TemplateView.as_view(template_name='site_index.html'),
   #     name='home'),
   re_path(r'^oca',
       HomePage.as_view(),
       name='home'),
#    url(r'^/?$', HomePage.as_view(), name='home'),
] + urlpatterns
