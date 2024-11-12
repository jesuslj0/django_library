from functools import wraps
from django.http import Http404
from django.core.exceptions import PermissionDenied

#Decorador custom para editar modelo
def user_can_edit(model):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            objects = model.objects.all()
        
            try:
                element = objects.get(pk=kwargs['id'])
            except element.DoesNotExit:
                raise Http404
                
            if element.created_by == request.user:
                return func(request, *args, **kwargs)
            
            raise PermissionDenied
        return wrapper
    return decorator

# Decorador para eliminar un modelo
def user_can_delete(model):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            objects = model.objects.all()
        
            try:
                element = objects.get(pk=kwargs['id'])
            except element.DoesNotExit:
                raise Http404
                
            if element.created_by == request.user:
                return func(request, *args, **kwargs)
            
            raise PermissionDenied
        return wrapper
    return decorator