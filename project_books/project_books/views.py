from django.shortcuts import render, redirect
from .forms import SearchForm, ContactForm, LoginForm, RegisterForm
from django.core.mail import send_mail
from django.conf import settings
from books.models import Autor, Libro, Editorial, Contacto
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

# Vistas generales (basadas en funciones)
# def root_view(request):
#     if request:
#         raise Http404('Página no encontrada')
    
# def home_view(request):
#     search_form = SearchForm()

#     context = {
#         'search_form': search_form
#     }

#     return render(request, 'general/home.html', context)

# def contacto_view(request):

#     if request.POST: 
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             coment = form.cleaned_data['coment']

#             send_mail(
#                 subject,
#                 f'Mensaje de nuestro seguidor {name}: {coment}',
#                 settings.EMAIL_HOST_USER,
#                 ['jesuslopj0@gmail.com'],
#                 fail_silently=False,
#             )

#             new_contact = Contacto.objects.create(
#                 nombre=name,
#                 email=email,
#                 motivo=subject,
#                 mensaje=coment, 
#             )

#             new_contact.save()

#             context = {
#                 'success': True
#             }

#             return render(request, 'general/contacto.html', context)

#         else:
#             context = {
#                 'form': form,
#                 'success': False,
#             }

#             return render(request, 'general/contacto.html', context)
        
#     form = ContactForm()

#     context = {
#         'form': form 
#     }

#     return render(request, 'general/contacto.html', context)

def search_view(request):

    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        query = search_form.cleaned_data['q']

        if query:

            autores = Autor.objects.filter(nombre__icontains=query) | Autor.objects.filter(apellido__icontains=query) # Union de querysets
            editoriales = Editorial.objects.filter(nombre__icontains=query)
            libros = Libro.objects.filter(titulo__icontains=query)

            context = {
                'autores': autores,
                'libros': libros,
                'editoriales': editoriales,
                'search_form': search_form,
            }

            return render(request, 'general/search.html', context)
    else: 
        search_form = SearchForm()

    context = {
        'search_form': search_form
    }

    return render(request, 'general/search.html', context)

def login_view(request):
    if request.POST:
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                context= {
                'login_form': login_form,
                'error': True,
                'error_message': 'Usuario no válido',
                }
                return render(request, 'general/login.html', context)

        else:
            context= {
                'login_form': login_form,
                'error': True,
            }

            return render(request, 'general/login.html', context)
    else:
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

    return render(request, 'general/login.html', context)

def logout_view(request): 
    logout(request)
    return redirect(reverse('home'))

def register_view(request):

    if request.POST:
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']

            new_user = User.objects.create(
                username = username,
                first_name = first_name,
                last_name = last_name,
                password = password,
                email = email,
            )

            new_user.save()

            context= {
                'msg': f'Usuario {username} registrado correctamente',
            }

            return render(request, 'general/register.html', context)

        else:
            context= {
                'register_form': register_form,
                'error': True,
            }

            return render(request, 'general/register.html', context)
    else:
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

    return render(request, 'general/register.html', context)

# Vistas basadas en Clases

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

class HomeView(TemplateView):
    template_name = 'general/home.html'

class ContactView(FormView):
    template_name = "general/contacto.html"
    form_class = ContactForm
    success_url = "/contacto/"

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        coment = form.cleaned_data['coment']

        send_mail(
            subject,
            f'Mensaje de nuestro seguidor {name}: {coment}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        
        return super().form_valid(form)

    

    