from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

    def __str__(self):
        return self.nombre

