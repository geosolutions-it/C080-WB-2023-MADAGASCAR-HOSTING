from django.template import RequestContext, loader
from partenaire.models import Partenaire
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render


def index(request):
    partenaire_list = Partenaire.objects.all()
    return render(request, 'partenaire/partenaire_liste.html',
        RequestContext(request, {'partenaire_list': partenaire_list}))
