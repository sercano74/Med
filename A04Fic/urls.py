from django.urls import path
from .views import *

app_name = 'A04Fic'

urlpatterns = [

    path("Fichas/",Fichas, name="Fichas"),
    path('FichaCreate/',FichaCreate,name="FichaCreate"),
    path('FichaRead/<int:pk>',FichaRead,name="FichaRead"),
    path('FichaUpdate/<int:pk>',FichaUpdate,name="FichaUpdate"),
    # path('PacienteDelete/<int:pk>',PacienteDelete,name="PacienteDelete"),

    # path('Medicos/',Medicos, name='Medicos'),
    # path('MedicoCreate/',MedicoCreate,name="MedicoCreate"),
    # path('MedicoRead/<int:pk>',MedicoRead,name="MedicoRead"),
    # path('MedicoUpdate/<int:pk>',MedicoUpdate,name="MedicoUpdate"),
    # path('MedicoDelete/<int:pk>',MedicoDelete,name="MedicoDelete"),

    # path('contactar/', contactar, name="contactar"),
    # path('perfilView/', perfilView, name="perfilView"),
    # path('perfilEdit/', perfilEdit, name="perfilEdit"),

]