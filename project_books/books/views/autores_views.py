from django.shortcuts import render
from project_books.forms import SearchForm

from books.models import Autor
autores_objects = Autor.objects.all()

def autores_view(request):

    search_form = SearchForm()

    autores = []

    for i in autores_objects:
        autores.append({
            'id': i.id,
            'nombre': i.nombre,
            'apellido': i.apellido,
        })

    context = {
        'items': autores,
        'search_form': search_form,
    }

    return render(request, 'books/autores.html', context)   

def autor_detail_view(req, id): 

    context = {
        'autor': None
    } 

    for autor in autores_objects:
        if autor.id == id:
            context['autor'] = autor

    return render(req, 'books/autor_detail.html', context)