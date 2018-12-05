from django.contrib.syndication.views import Feed
from blog.models import Entrada
from django.utils.feedgenerator import Atom1Feed


class RssEntradas(Feed):

    title = "Miblog"
    link = "/blog/"
    description = "Las Ultimas entradas de mi Miblog."

    def items(self):
        return Entrada.objects.all().order_by('-fecha')[:5]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.texto


class AtomSiteNewsFeed(RssEntradas):
    feed_type = Atom1Feed
    subtitle = RssEntradas.description