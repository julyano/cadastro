from django.contrib import admin
	
from .models import UsuarioModel
	
@admin.register(UsuarioModel)
class UsuarioModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'datanascimento')
    search_fields = ['nome', 'cpf', ]
    list_per_page = 5
