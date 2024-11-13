#Procesador de contexto custom 

def get_user_logged(request):
    user = request.user
    return {
        'user_logged': user
    }

import datetime as dt

def get_current_year(request):
    year = dt.datetime.now().year
    return {
        'current_year': year
    }