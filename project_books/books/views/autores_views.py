from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from books.models import Autor
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from project_books.forms import SearchForm
from django.urls import reverse_lazy
from books.decorators import user_can_edit, user_can_delete
from django.utils.decorators import method_decorator

"""def autores_view(request):

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
"""
""""def autor_detail_view(req, id): 

    context = {
        'autor': None
    } 

    for autor in autores_objects:
        if autor.id == id:
            context['autor'] = autor

    return render(req, 'books/autor_detail.html', context)
"""

class AutoresListView(ListView):
    model = Autor
    template_name = 'autor/AutoresList.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["search_form"] = SearchForm()
        return context


class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autor/AutorDetail.html'
    context_object_name = 'autor'
    pk_url_kwarg = 'id'


class AutorCreateView(CreateView):
    model = Autor
    template_name = 'autor/AutorCreate.html'
    context_object_name = 'autor'
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'biografia']

    def get_success_url(self):
        return reverse_lazy('autores:detail', kwargs={'id': self.object.id})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

@method_decorator(user_can_edit(Autor), name='dispatch')
class AutorUpdateView(UpdateView):
    model = Autor
    template_name = 'autor/AutorUpdate.html'
    pk_url_kwarg = 'id'
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'biografia']

    def get_success_url(self):
        return reverse_lazy('autores:detail', kwargs={'id': self.object.id})

@method_decorator(user_can_delete(Autor), name='dispatch')
class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autor/AutorDelete.html'
    success_url = reverse_lazy('autores:list') 
    pk_url_kwarg = 'id'


