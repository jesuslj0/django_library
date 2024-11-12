from django.urls import path
from books.views import LibrosListView, LibroDetailView, LibroCreateView, LibroUpdateView, LibroDeleteView
from django.contrib.auth.decorators import login_required

app_name = 'libros'

urlpatterns = [
    path('list/', login_required(LibrosListView.as_view()), name='list'),
    path('detail/<int:id>/', login_required(LibroDetailView.as_view()), name='detail'),
    path('create/', login_required(LibroCreateView.as_view()), name='create'),
    path('update/<int:id>', login_required(LibroUpdateView.as_view()), name='update'),
    path('delete/<int:id>/', login_required(LibroDeleteView.as_view()), name='delete'),
]