#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView


class HomePage(TemplateView):

    template_name = 'oca.html'

    def get_context_data(self):
        oca_statics = os.path.join(settings.STATIC_ROOT, 'oca')
        if not os.path.exists(oca_statics):
            oca_statics = os.path.join(os.path.dirname(__file__),
                    'static/oca')

        fokontany = os.listdir(os.path.join(oca_statics, 'fokontany'))
        fkt = [os.path.splitext(fok)[0] for fok in fokontany]

        bati = os.listdir(os.path.join(oca_statics, 'bati'))
        eau = os.listdir(os.path.join(oca_statics, 'eau'))
        route = os.listdir(os.path.join(oca_statics, 'route'))

        return {
            'fkt': fkt,
            'f': oca_statics,
            'bati': bati,
            'eau': eau,
            'route': route,
            }
