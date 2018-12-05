from blog.models import Entrada,Categoria
from django.views.generic import ListView,DetailView,DayArchiveView
from django.shortcuts import get_object_or_404
from django.views.generic import MonthArchiveView
from django.shortcuts import render_to_response
from django.views.generic import YearArchiveView
from heapq import merge


class ListaEntradas(ListView):
        '''Entradas del blog'''
        queryset=Entrada.objects.filter(estatus='p')
        context_object_name='entradas'
        template_name='blog/entradas.html'
        paginate_by=5


class Detalles(DetailView):
        model=Entrada
        context_object_name='entradas'
        template_name='blog/detalles.html'


class ListaCategorias(ListView):
    """Retorna las Entradas por tipo de Categorias """
    template_name = 'blog/categorias.html'

    def get_queryset(self):
        self.categoria=get_object_or_404(Categoria, slug__exact=self.kwargs['slug'])
        return Entrada.objects.filter(categoria=self.categoria)

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['entradas']= Entrada.objects.filter(categoria=self.categoria)
        context['categorias']= Categoria.objects.get(nombre=self.categoria)
        return context


class  EntradasDia( DayArchiveView):
        """REntradas por dia"""
        queryset=Entrada.objects.order_by('fecha')
        template_name='blog/entradas_dia.html'
        date_field = 'fecha'
        context_object_name='entradas'
        month_format = '%m'


class EntradasMes(MonthArchiveView):
        """Entradas por mes"""
        queryset=Entrada.objects.order_by('fecha')
        template_name='blog/entradas_mes.html'
        date_field = 'fecha'
        month_format = '%m'
        context_object_name='entradas'


class  EntradasYear(YearArchiveView):
        """Entradas por ano"""
        queryset=Entrada.objects.order_by('fecha')
        template_name='blog/entradas_año.html'
        date_field = 'fecha'
        context_object_name='entradas'
        make_object_list='True'


def buscar(request):
    def unir(lista1, lista2):
        lista = []
        for x in lista1:
            lista.append(x)
        for x in lista2:
            lista.append(x)
        return lista
    query = request.GET.get('q', '')
    if query:
        results = Entrada.objects.filter(titulo__icontains=query)
        #resultsb = Entrada.objects.filter(texto__icontains=query)
        #results = unir(resultsa,resultsb)
    else:
        results = []
    return render_to_response("blog/search.html", {
        "results": results,
        "query": query
    })
