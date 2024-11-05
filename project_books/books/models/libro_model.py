from django.db import models
from .autor_model import Autor
from .editorial_model import Editorial
from thumbnails.fields import ImageField


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    autores = models.ManyToManyField(Autor)  # Muchos a muchos
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)  # Uno a muchos
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    portada = ImageField(
        verbose_name='portada',
        upload_to='books/img',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.titulo