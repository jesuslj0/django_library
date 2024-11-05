
from django.urls import path
from .views import autores_view, editoriales_view, libros_view, autor_detail_view, libro_detail_view

app_name = 'books'

urlpatterns = [
    path('autores/', autores_view, name='autores_list'),
    path('autores/<int:id>/', autor_detail_view, name='autor_detail'),

    path('editoriales/', editoriales_view, name='editoriales_list'),

    path('libros/<int:id>', libro_detail_view, name='libro_detail'),
    path('libros/', libros_view, name='libros_list'),
]

