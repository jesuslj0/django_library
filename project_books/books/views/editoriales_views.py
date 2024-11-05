 
from django.shortcuts import render
from books.models import Editorial
from project_books.forms import SearchForm

editoriales_objects = Editorial.objects.all()

def editoriales_view(request): 

    search_form = SearchForm()

    editoriales = []

    for i in editoriales_objects:
        editoriales.append({
            'nombre': i.nombre,
            'direccion': i.direccion,
            'ciudad': i.ciudad,
            'pais': i.pais,
        })
    
    context = {
        'items': editoriales,
        'search_form': search_form,
    }

    
    return render(request, 'books/editoriales.html', context)