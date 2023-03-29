from django.template import RequestContext, loader
from partenaire.models import Partenaire
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response


def index(request):
    partenaire_list = Partenaire.objects.all()
    return render_to_response('partenaire/partenaire_liste.html',
        RequestContext(request, {'partenaire_list': partenaire_list}))
