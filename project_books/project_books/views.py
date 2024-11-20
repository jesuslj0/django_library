from django.http.response import HttpResponse as HttpResponse
from .forms import SearchForm, ContactForm, LoginForm, RegisterForm
from django.core.mail import send_mail
from django.conf import settings
from books.models import Autor, Libro, Editorial, Contacto
from django.contrib.auth.models import User

# Vistas generales (basadas en funciones)

"""def root_view(request):
    if request:
        raise Http404('Página no encontrada')
"""
    
"""def home_view(request):
    search_form = SearchForm()

    context = {
        'search_form': search_form
    }

    return render(request, 'general/home.html', context)
"""

"""def contacto_view(request):

    if request.POST: 
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            coment = form.cleaned_data['coment']

            send_mail(
                subject,
                f'Mensaje de nuestro seguidor {name}: {coment}',
                settings.EMAIL_HOST_USER,
                ['jesuslopj0@gmail.com'],
                fail_silently=False,
            )

            new_contact = Contacto.objects.create(
                nombre=name,
                email=email,
                motivo=subject,
                mensaje=coment, 
            )

            new_contact.save()

            context = {
                'success': True
            }

            return render(request, 'general/contacto.html', context)

        else:
            context = {
                'form': form,
                'success': False,
            }

            return render(request, 'general/contacto.html', context)
        
    form = ContactForm()

    context = {
        'form': form 
    }

    return render(request, 'general/contacto.html', context)
"""

"""def search_view(request):

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
"""

"""def login_view(request):
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
"""

"""def logout_view(request): 
    logout(request)
    return redirect(reverse('home'))
"""

"""def register_view(request):

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
"""

# Vistas basadas en Clases

from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils import translation
from django.http import HttpResponseRedirect

class HomeView(TemplateView):
    template_name = 'general/home.html'


class MessageMixin:
    success_message = ''
    error_message = ''

    def form_valid(self, form):
        if self.success_message:
            messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.error_message:
            messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class LoginView(MessageMixin, LoginView):
    template_name = 'general/login.html'
    authentication_form = LoginForm
    success_message = 'Iniciaste sesión correctamente.'
    error_message = 'Error en el inicio de sesión.'


class LogoutView(LogoutView):
    next_page = reverse_lazy('login')
    error_message = "Error al cerrar sesión."

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Has cerrado sesión. ¡Hasta pronto!")
        return super().dispatch(request, *args, **kwargs)


class ContactView(MessageMixin, FormView):
    model = Contacto
    template_name = "general/contacto.html"
    form_class = ContactForm
    success_url = "/contacto/"
    success_message = "Formulario enviado correctamente. Gracias por escribirnos!"
    error_message = "Error al enviar el formulario."

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        coment = form.cleaned_data['coment']

        new_contact = Contacto.objects.create(
                nombre=name,
                email=email,
                motivo=subject,
                mensaje=coment, 
            )
        new_contact.save()

        send_mail(
            subject,
            f'Mensaje de nuestro seguidor {name}: {coment}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return super().form_valid(form)
    

class MultiModelSearchView(TemplateView):
    template_name = 'general/search.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")  # Obtenemos el término de búsqueda desde la URL
        context = self.get_context_data(query=query)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = kwargs.get("query")

        # Realiza la búsqueda en múltiples modelos usando Q para filtros avanzados
        if query:
            # Buscar en el modelo Libro
            context['libros'] = Libro.objects.filter(
                Q(titulo__icontains=query) | Q(autores__nombre__icontains=query) | Q(autores__apellido__icontains=query)
            )

            # Buscar en el modelo Autor
            context['autores'] = Autor.objects.filter(
                Q(nombre__icontains=query) | Q(apellido__icontains=query)
            )

            # Buscar en el modelo Editorial
            context['editoriales'] = Editorial.objects.filter(
                nombre__icontains=query
            )
            context['search_form'] = SearchForm()
        else:
            # Si no hay búsqueda, se devuelve una lista vacía o puedes omitir esta sección
            context['libros'] = Libro.objects.none()
            context['autores'] = Autor.objects.none()
            context['editoriales'] = Editorial.objects.none()
            context['search_form'] = SearchForm()

        return context
    

class RegisterView(CreateView):
    model = User
    template_name = 'general/register.html'
    success_url = reverse_lazy("login")
    form_class = RegisterForm

    def form_valid(self, form):
        messages.success(self.request, 'Usuario registrado correctamente!')
        return super().form_valid(form)
    