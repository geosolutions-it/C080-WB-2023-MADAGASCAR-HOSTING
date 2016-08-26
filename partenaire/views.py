from django.http import HttpResponse



def index(request):
    return HttpResponse("Geonode est une plateforme  de gestion de risque et catastrophe naturelle")