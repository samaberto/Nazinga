from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

   #Usamos include para  cargamos la url de nuestro blog
   url(r'^admin/', include(admin.site.urls)),
   (r'', include('blog.urls')),
)