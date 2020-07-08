from modeltranslation.translator import translator, TranslationOptions
from partenaire.models import Partenaire

class PartenaireTranslationOptions(TranslationOptions):
    fields = ('description', )

translator.register(Partenaire, PartenaireTranslationOptions)
