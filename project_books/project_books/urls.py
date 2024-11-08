"""project_books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.conf import settings

from .views import login_view, logout_view
from .views import HomeView, ContactView, MultiModelSearchView, RegisterView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('contacto/', ContactView.as_view(), name='contacto'),
    path('search/', MultiModelSearchView.as_view(), name='search'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('autores/', include('books.urls.autores_urls', namespace='autores')),
    path('editoriales/', include('books.urls.editoriales_urls', namespace='editoriales')),
    path('libros/', include('books.urls.libros_urls', namespace='libros')),

] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:  # Solo sirve archivos de medios en modo de desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

