from django.shortcuts import render, redirect
from .models import user_role_map

# Create your views here.

def app_home(request):
    return render(request, 'appuser/home.html')


def redirector(request):
    actor = user_role_map.objects.filter(stamp_user = request.user)[0]    
    if actor.role.role_name == 'STUDENT':
        return redirect('lead-home')
    elif actor.role.role_name == 'TEACHER':
        return redirect('lead-home')
    elif actor.role.role_name == 'LIBRARY':
        return redirect('lead-home')
    elif actor.role.role_name == 'LEAD':
        return redirect('lead-home') 
    elif actor.role.role_name == 'MANAGEMENT':
        return redirect('lead-home') 
