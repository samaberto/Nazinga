from django import template
from blog.models import Entrada

register = template.Library()

#@register.inclusion_tag('blog/tags/entradas.html')
def ultimas_entradas(n=5):
    return {'template': template,
        'ultimas_entradas': Entrada.objects.filter(estatus='p')[:n]}

register.simple_tag(ultimas_entradas)