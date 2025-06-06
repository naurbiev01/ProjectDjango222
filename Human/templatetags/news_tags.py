from django.db.models import Count, F
from django.core.cache import cache
from unicodedata import category

from Human.models import Category
from django import template

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('Human/list_categories.html')
def show_categories(arg1='Список', arg2='категорий'):
    # categories = Category.objects.all()
    # categories = Category.objects.annotate(cnt=Count('humans')).filter(cnt__gt=0)
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.annotate(cnt=Count('humans', filter=F('humans__is_published'))).filter(cnt__gt=0)
        cache.set('categories', categories, 60)
    return {'categories': categories, 'arg1': arg1, 'arg2': arg2}