<<<<<<< HEAD
from django.template import RequestContext, loader
from partenaire.models import Partenaire
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response


def index(request):
    partenaire_list = Partenaire.objects.all()
    return render_to_response('partenaire/partenaire_liste.html',
        RequestContext(request, {'partenaire_list': partenaire_list}))
=======
from django.http import HttpResponse



def index(request):
    return HttpResponse("Geonode est une plateforme  de gestion de risque et catastrophe naturelle")
>>>>>>> 9c269c01542befb8fbb9791076aa2b98dd31892e
