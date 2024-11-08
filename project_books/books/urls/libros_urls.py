from django.urls import path
from books.views import LibrosListView, LibroDetailView, LibroCreateView, LibroUpdateView, LibroDeleteView

app_name = 'libros'

urlpatterns = [
    path('list/', LibrosListView.as_view(), name='list'),
    path('detail/<int:id>/', LibroDetailView.as_view(), name='detail'),
    path('create/', LibroCreateView.as_view(), name='create'),
    path('update/<int:id>', LibroUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', LibroDeleteView.as_view(), name='delete'),
]