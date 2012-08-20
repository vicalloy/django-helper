# -*- coding: UTF-8 -*-
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def getvars(request, excludes):
    getvars = request.GET.copy()
    excludes = excludes.split(',')
    for p in excludes:
        if p in getvars:
            del getvars[p]
        if len(getvars.keys()) > 0:
            return "&%s" % getvars.urlencode()
        else:
            return ''

@register.simple_tag(takes_context=True)
def get_setting(context, key, default_val, as_key=None):
    """ 
    get val form settings and set to context
      {% load djangohelper_tags %}
      {% get_setting "key" default_val "as_key" %}
      {{ as_key }}
    """
    as_key = as_key if as_key else key
    if ("%s" % default_val).startswith('$.'):
        default_val = getattr(settings, default_val[2:])
    val = getattr(settings, key, default_val)
    context[as_key] = val
    return ''
