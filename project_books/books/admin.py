from django.contrib import admin
from .models.autor_model import Autor
from .models.editorial_model import Editorial
from .models.libro_model import Libro 
from .models.contacto_model import Contacto

# Admin Actions
def export_to_csv(LibroAdmin, request, queryset):
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    
    writer.writerow(['Titulo', 'fecha_publicacion', 'ISBN', 'creado_por', 'descripcion'])
    for book in queryset:
        writer.writerow([book.titulo, book.fecha_publicacion, book.isbn, book.created_by, book.descripcion])
    
    return response

export_to_csv.short_description = "Exportar libros seleccionados a CSV"


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
    actions = [export_to_csv, ]

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 
                    'email', 
                    'motivo',
                    'mensaje']

