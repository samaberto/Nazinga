from django import template
from blog.models import Categoria

register = template.Library()

#register.inclusion_tag('blog/tags/categorias.html')
def ultimas_categorias(n=5):
    return {'template': template,
        'ultimas_categorias': Categoria.objects.filter()[:n]}


register.simple_tag(ultimas_categorias)