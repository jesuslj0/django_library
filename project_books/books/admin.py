from django.contrib import admin
from .models.autor_model import Autor
from .models.editorial_model import Editorial
from .models.libro_model import Libro 
from .models.contacto_model import Contacto

# Register your models here.

class LibroInline(admin.StackedInline):
    model = Libro
    extra = 1

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fecha_nacimiento']


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'ciudad', 'pais']
    inlines = [LibroInline]

@admin.register(Libro)
class LIbroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 
                    'fecha_publicacion', 
                    'editorial', 'isbn',
                    'portada']
    search_fields = ['titulo', 'autores__nombre']
    list_filter = ['fecha_publicacion']

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 
                    'email', 
                    'motivo',
                    'mensaje']


# Admin Login:
# user: jesus
# password: django123

        