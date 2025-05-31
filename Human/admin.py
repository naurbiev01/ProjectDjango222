from django.contrib import admin
from django.template.defaultfilters import title
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.

from .models import Humans, Category

class HumansAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Humans
        fields = '__all__'



class HumansAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'created_at', 'updated_at', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('id', 'is_published')
    list_editable = ('is_published', 'category')
    fields = ('title', 'content', 'created_at', 'updated_at', 'photo', 'get_photo', 'category', 'is_published')
    readonly_fields = ('get_photo', 'created_at', 'updated_at')
    form = HumansAdminForm


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото нет'

    get_photo_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Humans, HumansAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'




