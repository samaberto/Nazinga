from django.conf.urls import patterns, include, url
from blog.models import Entrada
from blog.views import ListaEntradas,Detalles,ListaCategorias
from blog.views import EntradasDia
from blog.views import EntradasMes
from blog.views import EntradasYear
from blog.feeds import RssEntradas, AtomSiteNewsFeed
#from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap


info_dict = {
    'queryset':Entrada.objects.filter(estatus='p'),
    'date_field': 'fecha',
   }
"""
sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': GenericSitemap(info_dict, priority=0.6),
}
"""
urlpatterns = patterns('',
                       url(r'^$', ListaEntradas.as_view(template_name='blog/bienvenidos.html')),
                       url(r'^buscar/$', 'blog.views.buscar'),
                       url(r'^blog/$', ListaEntradas.as_view()),
                       url(r'^blog/entradas/(?P<slug>[^\.]+).html', Detalles.as_view(),
        name='entradas'),
                       url(  r'^blog/categorias/(?P<slug>[^\.]+).html', ListaCategorias.as_view(),
        name='categorias'),

                       url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})$',
        EntradasDia.as_view(), name='entradas'),
                       url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/$',
        EntradasMes.as_view(), name='entradas'),
                       url(r'^blog/(?P<year>\d{4})/$',
        EntradasYear.as_view(), name='entradas'),
                       url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'', include('django.contrib.flatpages.urls')),
                       (r'^blog/feed/$', RssEntradas()),
                       [r'^blog/atom/$', AtomSiteNewsFeed()],
                        #(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
                        #(r'^ckeditor/', include('ckeditor.urls')),
                       )