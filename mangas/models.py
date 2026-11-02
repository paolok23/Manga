from django.db import models

class Manga(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    portada = models.ImageField(upload_to='portadas/')
    fondo = models.ImageField(upload_to='fondos_mangas/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Capitulo(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='capitulos')
    numero_capitulo = models.DecimalField(max_digits=5, decimal_places=1)
    titulo_capitulo = models.CharField(max_length=200, blank=True)
    musica_fondo = models.FileField(upload_to='musica_capitulos/', blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['numero_capitulo']

    def __str__(self):
        return f"{self.manga.titulo} - Cap {self.numero_capitulo}"

class Pagina(models.Model):
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE, related_name='paginas')
    imagen = models.ImageField(upload_to='mangas_paginas/')
    numero_pagina = models.PositiveIntegerField()

    class Meta:
        ordering = ['numero_pagina']

    def __str__(self):
        return f"Pág. {self.numero_pagina} (Cap {self.capitulo.numero_capitulo})"