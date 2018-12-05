from django.contrib import admin
from blog.models import Entrada, Categoria

class AdminEntrada(admin.ModelAdmin):

    list_display = ('titulo', 'autor', 'fecha', 'estatus' )
    prepopulated_fields = {"slug": ("titulo",)}
    list_filter = ('titulo', 'fecha')
    ordering = ('-fecha',)
    search_fields = ('titulo', 'texto')
    actions = ['publicar_entradas', 'marcar_como_borrador']

    def publicar_entradas(self, request, queryset):
        rows_updated = queryset.update(estatus='p')
        if rows_updated == 1:
            message_bit = "1 entrada fue"
        else:
            message_bit = "%s entradas fueron" % rows_updated
        self.message_user(request, "%s publicadas exitosamente." % message_bit)
    publicar_entradas.short_description = "Marcar como publicadas"

    def marcar_como_borrador(self, request, queryset):
        rows_updated = queryset.update(estatus='b')
        if rows_updated == 1:
            message_bit = "1 entrada fue"
        else:
            message_bit = "%s entradas fueron" % rows_updated
        self.message_user(request, "%s marcadas como borrador." % message_bit)
    marcar_como_borrador.short_description="Marcar como borradores"

admin.site.register(Entrada, AdminEntrada)

class AdminCategoria(admin.ModelAdmin):
    list_display= ('nombre','slug')

admin.site.register(Categoria,AdminCategoria)