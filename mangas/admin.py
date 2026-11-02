from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Capitulo, Manga, Pagina


class PaginaInline(admin.TabularInline):
  model = Pagina
  extra = 0


@admin.register(Capitulo)
class CapituloAdmin(admin.ModelAdmin):
  list_display = (
      'manga',
      'numero_capitulo',
      'titulo_capitulo',
      'boton_subida_masiva',
  )
  inlines = [PaginaInline]

  def boton_subida_masiva(self, obj):
    if obj.id:
      # Genera el enlace directo a la ruta de subida masiva de este capítulo específico
      url = reverse('subida_masiva', args=[obj.id])
      return format_html(
          '<a class="button" href="{}" style="background-color: #ff4757;'
          ' color: white; padding: 6px 12px; border-radius: 4px; font-weight:'
          ' bold; text-decoration: none;">📂 Subir Páginas Masivas</a>',
          url,
      )
    return 'Guarda el capítulo primero'

  boton_subida_masiva.short_description = 'Acción Rápida'


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
  list_display = ('titulo',)