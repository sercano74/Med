from django.contrib import admin
from .models import *

# Register your models here

class CtgPostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','active','created')
admin.site.register(CtgPost, CtgPostAdmin)


class EtqPostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','active','created')
admin.site.register(EtqPost, EtqPostAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author','published','created','category','post_tags'  )
    ordering=('-created','author')
    search_fields=('title','content','author__username','category__name')
    list_filter=('author','category','tags')

    def post_tags(self,obj):
        print('self ------------------>>  ', self)#es la app blog
            #self ------------------>>   Ap01Blog.PostAdmin
        print('obj ------------------>>  ', obj)  #es el objeto Post
            #obj ------------------>>   Diseños Actuales
        return ' - '.join([t.name for t in obj.tags.all().order_by('name')])
    # Definimos un nuevo rótulo en el sitio de administración
    post_tags.short_description='Etiquetas'
admin.site.register(Post, PostAdmin)




class AboutAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('description','created')
admin.site.register(About, AboutAdmin)


class LinkAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','key','url','icon')
admin.site.register(Link, LinkAdmin)
