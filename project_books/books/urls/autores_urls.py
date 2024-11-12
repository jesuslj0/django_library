from django.urls import path
from books.views import AutoresListView, AutorDetailView, AutorCreateView, AutorUpdateView, AutorDeleteView
from django.contrib.auth.decorators import login_required

app_name = 'autores'

urlpatterns = [
    path('list/', login_required(AutoresListView.as_view()), name='list'),
    path('detail/<int:id>/', login_required(AutorDetailView.as_view()), name='detail'),
    path('create/', login_required(AutorCreateView.as_view()), name='create'),
    path('update/<int:id>/', login_required(AutorUpdateView.as_view()), name='update'),
    path('delete/<int:id>/', login_required(AutorDeleteView.as_view()), name='delete'),
]

