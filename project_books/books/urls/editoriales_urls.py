from django.urls import path
from books.views import EditorialesListView, EditorialDetailView, EditorialCreateView, EditorialUpdateView, EditorialDeleteView

app_name = 'editoriales'

urlpatterns = [
    path('list/', EditorialesListView.as_view(), name='list'),
    path('detail/<int:id>/', EditorialDetailView.as_view(), name='detail'),
    path('create', EditorialCreateView.as_view(), name='create'),
    path('update/<int:id>', EditorialUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', EditorialDeleteView.as_view(), name='delete'),
]

