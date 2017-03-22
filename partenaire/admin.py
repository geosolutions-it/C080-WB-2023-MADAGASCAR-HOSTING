from django.contrib import admin
from partenaire.models import Partenaire
from django.conf import settings
from modeltranslation.admin import TranslationAdmin

import autocomplete_light
# from autocomplete_light.contrib.taggit_tagfield import TagField, TagWidget

class MediaTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'modeltranslation/js/tabbed_translation_fields.js', )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',), }

    class Meta:
        fields = '__all__' # Or a list of the fields that you want to include in your form
        exclude = ()


class PartenaireAdmin(MediaTranslationAdmin):
    class Meta:
        model = Partenaire
        exclude = ()

    search_fields = ('nom_organisation', 'description',)
    # form = autocomplete_light.modelform_factory(Partenaire)


admin.site.register(Partenaire,PartenaireAdmin)
