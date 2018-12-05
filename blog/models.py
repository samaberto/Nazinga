from django.db import models
from django.db.models import permalink

ESTADO = (
    ('b', 'Borrador'),
    ('p', 'Publicado'),
    )

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural='Categorias'

    def __unicode__(self):
        return '%s' % self.nombre

    @permalink
    def get_absolute_url(self):
        return ('categorias', None, { 'slug': self.slug })


class Entrada(models.Model):

    titulo = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    autor= models.CharField(max_length=100)
    texto= models.TextField()
    fecha= models.DateTimeField(db_index=True, auto_now_add=True)
    estatus = models.CharField(max_length=1, choices=ESTADO)
    categoria= models.ManyToManyField(Categoria)

    class Meta:
        ordering=['-fecha']
        verbose_name_plural='Entradas'

    def __unicode__(self):
        return '%s' % self.titulo

    @permalink
    def get_absolute_url(self):
        return ('entradas', None, { 'slug': self.slug })