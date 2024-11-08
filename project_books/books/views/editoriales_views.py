 
from django.shortcuts import render
from books.models import Editorial
from project_books.forms import SearchForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class EditorialesListView(ListView):
    model = Editorial
    template_name = 'editorial/EditorialesList.html'


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'editorial/EditorialDetail.html'



class EditorialCreateView(CreateView):
    model = Editorial
    template_name = 'editorial/EditorialCreate.html'



class EditorialUpdateView(UpdateView):
    model = Editorial
    template_name = 'editorial/EditorialUpdate.html'


class EditorialDeleteView(DeleteView):
    model = Editorial
