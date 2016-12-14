from django.contrib import admin
<<<<<<< HEAD
from partenaire.models import Partenaire
from django.conf import settings
from modeltranslation.admin import TranslationAdmin

import autocomplete_light
from autocomplete_light.contrib.taggit_tagfield import TagField, TagWidget

class MediaTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class PartenaireAdmin(MediaTranslationAdmin):
    model = Partenaire
    search_fields = ('nom_organisation', 'description',)
    form =  form = autocomplete_light.modelform_factory(Partenaire)


admin.site.register(Partenaire,PartenaireAdmin)
=======

# Register your models here.
>>>>>>> 9c269c01542befb8fbb9791076aa2b98dd31892e
