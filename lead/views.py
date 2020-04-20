from django.shortcuts import render, redirect
from django.contrib import messages
# models
from django.contrib.auth.models import User
from appuser.forms import UserRegisterForm
from appuser.models import user_role_map, role_details
# forms
from mgmt.forms import managementForm
from lead.forms import leadForm


# Create your views here.
def lead_index(request):
    return render(request, 'lead/lead-index.html')


def create_management(request):
    if request.method == 'POST':
        form = managementForm(request.POST)
        form2 = UserRegisterForm(request.POST)
        if form.is_valid() and form2.is_valid():
            u = form2.cleaned_data.get('username')
            new_management = form.save(commit=False)
            form2.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f' {first_name} saved in system!')
            user = User.objects.filter(username__exact=u)[0]
            new_management.user_name = user
            new_management.save()
            user_role = role_details.objects.filter(role_name__exact='MANAGEMENT')[0]
            new_user = user_role_map(stamp_user=user, role=user_role)
            new_user.save()
            return redirect('add-management')

    else:
        form = managementForm()
        form2 = UserRegisterForm()
    return render(request, 'lead/save-user.html', {'form': form, 'form2': form2, 'title': 'Add management user'})



def create_leaduser(request):
    if request.method == 'POST':
        form = leadForm(request.POST)
        form2 = UserRegisterForm(request.POST)
        if form.is_valid() and form2.is_valid():
            u = form2.cleaned_data.get('username')
            new_lead = form.save(commit = False)
            form2.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f' {first_name} saved in system!')
            user = User.objects.filter(username__exact=u)[0]
            new_lead.user_name = user
            new_lead.save()
            user_role = role_details.objects.filter(role_name__exact='LEAD')[0]
            new_user = user_role_map(stamp_user=user, role=user_role)
            new_user.save()
            return redirect('add-leaduser')

    else:
        form = leadForm()
        form2 = UserRegisterForm()
    return render(request, 'lead/save-user.html', {'form': form, 'form2': form2, 'title': 'lead user'})