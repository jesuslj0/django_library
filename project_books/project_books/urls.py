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
from django.conf.urls.i18n import i18n_patterns
from .views import HomeView, ContactView, MultiModelSearchView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('home/', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('contacto/', ContactView.as_view(), name='contacto'),
    path('search/', MultiModelSearchView.as_view(), name='search'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('autores/', include('books.urls.autores_urls', namespace='autores')),
    path('editoriales/', include('books.urls.editoriales_urls', namespace='editoriales')),
    path('libros/', include('books.urls.libros_urls', namespace='libros')),
)

if settings.DEBUG:  # Solo sirve archivos de medios en modo de desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls')),
    ]