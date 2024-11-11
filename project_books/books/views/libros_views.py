 
from typing import Any
from books.models import Libro
from project_books.forms import SearchForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

"""
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
"""


class LibrosListView(ListView):
    model = Libro
    template_name = 'libro/LibrosList.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        return context


class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/LibroDetail.html'
    context_object_name = 'libro'
    pk_url_kwarg = 'id'


class LibroCreateView(CreateView):
    model = Libro
    template_name = 'libro/LibroCreate.html'
    fields = ['titulo', 'fecha_publicacion', 'autores', 'editorial', 'isbn']

    def get_success_url(self) -> str:
        return reverse_lazy('libros:detail', kwargs={"id": self.object.id})
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class LibroUpdateView(UpdateView):
    model = Libro
    template_name = 'libro/LibroUpdate.html'
    fields = ['titulo', 'fecha_publicacion', 'autores', 'editorial', 'isbn']
    pk_url_kwarg = 'id'

    def get_success_url(self) -> str:
        return reverse_lazy('libros:detail', kwargs={'id': self.object.id})


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libro/LibroDelete.html'
    success_url = reverse_lazy('libros:list') 
    pk_url_kwarg = 'id'