from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

admin.site.register(UserProfileProfessor)
admin.site.register(UserProfileStudent)
# admin.site.register(Faculty)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Room)
admin.site.register(Schedule)
admin.site.register(Registration)
admin.site.register(Homework)
admin.site.register(Submitting)
admin.site.register(Role)


@admin.register(Faculty)
class ProductAdmin(TranslationAdmin):
    list_display = ("name", )

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }