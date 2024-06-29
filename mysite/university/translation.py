from .models import Faculty
from modeltranslation.translator import TranslationOptions,register


@register(Faculty)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)


