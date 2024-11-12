from django.urls import path
from books.views import EditorialesListView, EditorialDetailView, EditorialCreateView, EditorialUpdateView, EditorialDeleteView
from django.contrib.auth.decorators import login_required

app_name = 'editoriales'

urlpatterns = [
    path('list/', login_required(EditorialesListView.as_view()), name='list'),
    path('detail/<int:id>/', login_required(EditorialDetailView.as_view()), name='detail'),
    path('create', login_required(EditorialCreateView.as_view()), name='create'),
    path('update/<int:id>', login_required(EditorialUpdateView.as_view()), name='update'),
    path('delete/<int:id>/', login_required(EditorialDeleteView.as_view()), name='delete'),
]

