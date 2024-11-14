from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('Usuarios/',include('A01Seg.urls', namespace='Seg')),
    path('Scope/',include('A04Fic.urls', namespace='Fic')),
    # path('Mantenedores/',include('A02Man.urls', namespace='Man')),
    # path('HorasMedicas/',include('A03Hrs.urls', namespace='Hrs')),
    # path('FichaMedica/',include('A04Fic.urls', namespace='Fic')),
    # path('Blog/',include('A05Blo.urls', namespace='Blo')),
    # path('Informes/',include('A06Inf.urls', namespace='Inf')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
