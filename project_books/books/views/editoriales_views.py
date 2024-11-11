 
from typing import Any
from books.models import Editorial
from project_books.forms import SearchForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

""" def editoriales_view(request): 

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
"""

class EditorialesListView(ListView):
    model = Editorial
    template_name = 'editorial/EditorialesList.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["search_form"] = SearchForm()
        return context


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'editorial/EditorialDetail.html'
    context_object_name = 'editorial'
    pk_url_kwarg = 'id'


class EditorialCreateView(CreateView):
    model = Editorial
    template_name = 'editorial/EditorialCreate.html'
    fields = ['nombre', 'direccion', 'ciudad', 'pais']

    def get_success_url(self):
        return reverse_lazy('editoriales:detail', kwargs={'id': self.object.id})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EditorialUpdateView(UpdateView):
    model = Editorial
    template_name = 'editorial/EditorialUpdate.html'
    pk_url_kwarg = 'id'
    fields = ['nombre', 'direccion', 'ciudad', 'pais']

    def get_success_url(self):
        return reverse_lazy('editoriales:detail', kwargs={'id': self.object.id})


class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = 'editorial/EditorialDelete.html'
    success_url = reverse_lazy('editoriales:list') 
    pk_url_kwarg = 'id'
