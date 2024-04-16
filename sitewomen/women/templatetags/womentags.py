from django import template
from django.db.models import Count

from sitewomen.women.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(posts_count=Count("posts")).filter(posts_count__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    tags = TagPost.objects.annotate(posts_count=Count("tags")).filter(posts_count__gt=0)
    return {'tags': tags}