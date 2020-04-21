from django.shortcuts import render, redirect
from django.contrib import messages
# models
from django.contrib.auth.models import User
from appuser.forms import UserRegisterForm
from appuser.models import user_role_map, role_details
from student.models import student_details
from mgmt.models import management_user
from lead.models import (lead_user,
                         grade_master,
                         subject_master,
                         subject_and_grade,
                         subject_grade_section,
                         grade_section_master
                         )
from teacher.models import teacher_details
# forms
from mgmt.forms import managementForm
from lead.forms import leadForm, busForm, createEventForm


# Create your views here.
def lead_index(request):
    student_count = student_details.objects.count()
    management_count = management_user.objects.count()
    lead_count = lead_user.objects.count()
    teacher_count = teacher_details.objects.count()
    context = {
        'student_count': student_count,
        'management_count': management_count,
        'lead_count': lead_count,
        'teacher_count': teacher_count
    }
    return render(request, 'lead/lead-index.html', context)


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
            user_role = role_details.objects.filter(
                role_name__exact='MANAGEMENT')[0]
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
            new_lead = form.save(commit=False)
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


def create_bus(request):
    if request.method == 'POST':
        form = busForm(request.POST)
        if form.is_valid():
            form.save()
            bsr = form.cleaned_data.get('bus_Route_start_to_end')
            messages.success(request, f' {bsr}  Bus Details saved in system!')
            return redirect('lead-home')
    else:
        form = busForm()
    return render(request, 'lead/single-form.html', {'form': form, 'title': 'Add-Bus-Info'})


def events(request):
    if request.method == 'POST':
        form = createEventForm(request.POST)
        if form.is_valid():
            form.save()
            bsr = form.cleaned_data.get('name')
            messages.success(request, f' {bsr}  saved!')
            return redirect('lead-home')
    else:
        form = createEventForm()
    return render(request, 'lead/single-form.html', {'form': form, 'title': 'annual leaves'})


def subject_create(request):
    gd = grade_master.objects.all()
    if request.method == "POST":
        sub = request.POST.get('subject_name')
        new_subject = subject_master(subject_name=sub)
        new_subject.save()
        for grade in request.POST.getlist('grado'):
            t = grade_master.objects.filter(grade_name=grade)[0]
            new_subject_grade = subject_and_grade(subject=new_subject, grade=t)
            new_subject_grade.save()
            grd_section_m = grade_section_master.objects.filter(grade=t)
            for gsm in grd_section_m:
                subject_section = subject_grade_section(
                    subject=new_subject, grade_section=gsm)
                subject_section.save()
        return redirect('lead-home')
    return render(request, 'lead/subject-form.html', {'grade': gd})
