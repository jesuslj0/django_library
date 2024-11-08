from django.urls import path
from books.views import AutoresListView, AutorDetailView, AutorCreateView, AutorUpdateView, AutorDeleteView

app_name = 'autores'

urlpatterns = [
    path('list/', AutoresListView.as_view(), name='list'),
    path('detail/<int:id>/', AutorDetailView.as_view(), name='detail'),
    path('create/', AutorCreateView.as_view(), name='create'),
    path('update/<int:id>/', AutorUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', AutorDeleteView.as_view(), name='delete'),
]