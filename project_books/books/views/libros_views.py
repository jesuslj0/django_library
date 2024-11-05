 
from django.shortcuts import render
from books.models import Libro
from project_books.forms import SearchForm

libros_objects = Libro.objects.all()

def libros_view(request):
    
    search_form = SearchForm()

    libros = []

    for libro in libros_objects:
        libros.append({
            'id': libro.id,
            'titulo': libro.titulo,
        })

    context = {
        'items': libros, 
        'search_form': search_form,
    }

    return render(request, 'books/libros.html', context)

def libro_detail_view(req, id): 

    context = {
        'libro': None
    } 

    for libro in libros_objects:
        if libro.id == id:
            context['libro'] = libro

    return render(req, 'books/libro_detail.html', context)
