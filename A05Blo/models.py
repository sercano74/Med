from django.db import models
from django.contrib.auth.models import User
from A01Seg.models import *

# from ckeditor.fields import RichTextField
# from fpdf import FPDF


# Create your models here.
class CtgPost(models.Model):
    name    = models.CharField(max_length=200, unique=True, verbose_name='Categoría')
    active  = models.BooleanField(default=True,verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True,verbose_name='Modificado')
    class Meta:
        verbose_name        = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering            = ['name']
    def __str__(self):
        return self.name


class EtqPost(models.Model):
    name    = models.CharField(max_length=200, unique=True, verbose_name='Etiqueta')
    active  = models.BooleanField(default=True,verbose_name='Activa')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creada')
    updated = models.DateTimeField(auto_now=True,verbose_name='Modificada')
    class Meta:
        verbose_name        = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering            = ['name']
    def __str__(self):
        return self.name


class Post(models.Model):
    # proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True,blank=True)
    category    = models.ForeignKey(CtgPost, on_delete=models.PROTECT, related_name='posts_4_categories',verbose_name='Categoría')
    title       = models.CharField(max_length=200, verbose_name='Título')
    excerpt     = models.TextField(verbose_name='Bajada')
    # content = RichTextField(verbose_name='Contenido')
    content     = models.TextField(verbose_name='Contenido')
    image       = models.ImageField(upload_to='posteos',null=True, blank=True, verbose_name='Imagen')
    tags        = models.ManyToManyField(EtqPost, verbose_name='Etiqueta')
    author      = models.ForeignKey(User, on_delete=models.PROTECT, related_name="posts_4_author",verbose_name='Autor')
    published   = models.BooleanField(default=False,verbose_name='Publicado')
    created     = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    updated     = models.DateTimeField(auto_now=True,verbose_name='Modificado')

    class Meta:
        verbose_name        = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering            = ['-created']

    def __str__(self):
        return self.title


class About(models.Model):
    description = models.CharField(max_length=400, unique=True, verbose_name='Descripción')
    created     = models.DateTimeField(auto_now_add=True,verbose_name='Creada')
    updated     = models.DateTimeField(auto_now=True,verbose_name='Modificada')

    class Meta:
        verbose_name        = 'Acerca de'
        verbose_name_plural = 'Acerca de'
        ordering            = ['-created']

    def __str__(self):
        return self.description


class Link(models.Model):
    key     = models.CharField(max_length=100,verbose_name='Key Link')
    name    = models.CharField(max_length=100,unique=True,verbose_name='Red Social')
    url     = models.URLField(max_length=100,blank=True,null=True,verbose_name='Enlace')
    icon    = models.CharField(max_length=400,blank=True,null=True,unique=True,verbose_name='Icono')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creada')
    updated = models.DateTimeField(auto_now=True,verbose_name='Modificada')

    class Meta:
        verbose_name        = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering            = ['-created','name']

    def __str__(self):
        return self.name

