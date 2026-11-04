import os
import re
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from .models import Capitulo, Manga, Pagina


def natural_sort_key(filename):
  """Función para ordenar números de forma natural (ej: 2 va antes que 10)."""
  return [
      int(text) if text.isdigit() else text.lower()
      for text in re.split(r'(\d+)', filename)
  ]


def lista_mangas(request):
  mangas = Manga.objects.all()
  return render(request, 'mangas/lista_mangas.html', {'mangas': mangas})


def detalle_manga(request, manga_id):
  manga = get_object_or_404(Manga, id=manga_id)
  capitulos = manga.capitulos.all()
  return render(
      request, 'mangas/detalle_manga.html', {'manga': manga, 'capitulos': capitulos}
  )


def leer_capitulo(request, capitulo_id):
  capitulo = get_object_or_404(Capitulo, id=capitulo_id)
  paginas = capitulo.paginas.all().order_by('numero_pagina')
  return render(
      request,
      'mangas/leer_capitulo.html',
      {'capitulo': capitulo, 'paginas': paginas},
  )


# ==========================================
# CAMBIOS DE SEGURIDAD:
# ==========================================
VALID_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.webp']

@user_passes_test(lambda u: u.is_staff)  # Restringe el acceso exclusivamente a administradores
def subida_masiva_paginas(request, capitulo_id):
  capitulo = get_object_or_404(Capitulo, id=capitulo_id)

  if request.method == 'POST':
    imagenes = request.FILES.getlist('imagenes')

    if imagenes:
      # Validar extensión de cada archivo por seguridad
      for imagen in imagenes:
        ext = os.path.splitext(imagen.name)[1].lower()
        if ext not in VALID_EXTENSIONS:
          messages.error(request, f"Archivo bloqueado: formato '{ext}' no permitido.")
          return redirect('subida_masiva', capitulo_id=capitulo.id)

      # Ordenamos usando la función de orden natural por número de archivo
      imagenes_ordenadas = sorted(
          imagenes, key=lambda f: natural_sort_key(f.name)
      )

      ultima_pagina = (
          capitulo.paginas.order_by('-numero_pagina').first().numero_pagina
          if capitulo.paginas.exists()
          else 0
      )

      for i, imagen in enumerate(imagenes_ordenadas):
        Pagina.objects.create(
            capitulo=capitulo,
            imagen=imagen,
            numero_pagina=ultima_pagina + i + 1,
        )

      return redirect('detalle_manga', manga_id=capitulo.manga.id)

  return render(
      request, 'mangas/subida_masiva.html', {'capitulo': capitulo}
  )