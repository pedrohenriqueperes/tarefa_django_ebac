# blog/admin.py
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')  # Ajuste os campos conforme necessário
    search_fields = ['titulo', 'conteudo']

# Registre o modelo e a classe de administração
admin.site.register(Post, PostAdmin)
