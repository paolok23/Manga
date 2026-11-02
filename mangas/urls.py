from django.urls import path
from . import views

urlpatterns = [
    # Página principal (Lista de mangas)
    path('', views.lista_mangas, name='lista_mangas'),
    
    # Detalle del manga y sus capítulos
    path('manga/<int:manga_id>/', views.detalle_manga, name='detalle_manga'),
    
    # Vista del lector de capítulos (con scroll y música de fondo)
    path('capitulo/<int:capitulo_id>/', views.leer_capitulo, name='leer_capitulo'),
    
    # Nueva ruta para la subida masiva de páginas por capítulo
    path('capitulo/<int:capitulo_id>/subida-masiva/', views.subida_masiva_paginas, name='subida_masiva'),
]