from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
# models
from django.contrib.auth.models import User
from appuser.models import user_role_map, role_details
from student.models import student_details
from mgmt.models import management_user
from lead.models import (lead_user,
                         grade_master,
                         subject_master,
                         subject_and_grade,
                         subject_grade_section,
                         grade_section_master,
                         bus_master
                         )
from teacher.models import teacher_details, department_head, department, grade_class_teacher

# forms
from appuser.forms import UserRegisterForm
from mgmt.forms import managementForm
from lead.forms import (leadForm,
                        busForm,
                        createEventForm,
                        subjectSectionForm
                        )

from student.forms import studentForm, studentAddressForm, studentBusForm
from teacher.forms import TeacherForm, departmentHeadForm, departmentForm, gradeClassTeacherForm

# Create your views here.

@login_required
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

@login_required
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

@login_required
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

@login_required
def add_student(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        adress_form = studentAddressForm(request.POST)
        bus_form = studentBusForm(request.POST)
        user_form = UserRegisterForm(request.POST)
        if form.is_valid() and adress_form.is_valid() and bus_form.is_valid() and user_form.is_valid():
            new_student = form.save(commit=False)
            first_name = form.cleaned_data.get('first_name')
            username = user_form.cleaned_data.get('username')
            user_form.save()
            user = User.objects.filter(username = username)[0]
            new_student.user_name = user
            new_student.save()
            user_role = role_details.objects.filter(role_name = 'STUDENT')[0]
            new_user_role = user_role_map(stamp_user = user, role = user_role)
            new_user_role.save()
            new_bus = bus_form.save(commit=False)
            new_bus.student = new_student
            new_bus.save()
            new_adress = adress_form.save(commit=False)
            new_adress.student = new_student
            new_adress.save()
            messages.success(request, f' {first_name} saved in system!')
            return redirect('add-student')
    else:
        form = studentForm()
        adress_form = studentAddressForm()
        bus_form = studentBusForm()
        user_form = UserRegisterForm()

    context = {
        'form': form,
        'adress_form': adress_form,
        'bus_form': bus_form,
        'user_form': user_form
    }


    return render(request, 'lead/add-student.html', context)

@login_required
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        user_form = UserRegisterForm(request.POST)
        if form.is_valid() and user_form.is_valid():
            new_teacher = form.save(commit=False)
            first_name = form.cleaned_data.get('first_name')
            username = user_form.cleaned_data.get('username')
            user_form.save()
            user = User.objects.filter(username = username)[0]
            new_teacher.user_name = user
            new_teacher.save()
            user_role = role_details.objects.filter(role_name = 'TEACHER')[0]
            new_user_role = user_role_map(stamp_user = user, role = user_role)
            new_user_role.save()
            messages.success(request, f' {first_name} saved in system!')
            redirect('add-teacher')

    else:
        form = TeacherForm()
        user_form = UserRegisterForm()
    context = {
        'form': form,
        'user_form': user_form,
        'title': 'Add teachers'
    }
    return render(request, 'lead/add-teachers.html', context)

@login_required
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

@login_required
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

@login_required
def subject_create(request):
    gd = grade_master.objects.all()
    subjects = subject_and_grade.objects.all()
    context = {
        'grade': gd,
        'subjects': subjects
    }
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
    return render(request, 'lead/subject-form.html', context)


@login_required
def subjectSection(request):
    if request.method == 'POST':
        form = subjectSectionForm(request.POST)
        sub = request.POST.get('subject_name')
        new_subject = subject_master(subject_name=sub)
        new_subject.save()
        grade_section_id = request.POST.get('grade_section')
        grade_section = grade_section_master.objects.get(id=grade_section_id)
        new_subject_grade = subject_and_grade(subject=new_subject, grade=grade_section.grade)
        new_subject_grade.save()
        new_subject_grade_section = subject_grade_section(subject=new_subject, grade_section=grade_section)
        new_subject_grade_section.save()
        return redirect('lead-home')
    else:
        form = subjectSectionForm()
    return render(request, 'lead/subjectSection.html', {'form': form, 'title': 'Subjects'})


@login_required
def departments(request):  # for mapping deparment heads to department
    if request.method == 'POST':
        form =departmentHeadForm(request.POST)
        form2 =departmentForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form2.save()
            name = form2.cleaned_data.get('name')
            d = department.objects.filter(name=name)[0]
            new_department_head = form.save(commit=False)
            new_department_head.department = d
            new_department_head.save()
            return redirect('departments')
    else:
        dept = department_head.objects.all()
        form = departmentHeadForm()
        form2 = departmentForm()

        context = {
            'form': form,
            'departments': dept,
            'form2': form2
        }
    return render(request, 'lead/departments.html', context)



@login_required
def add_classteacher(request):
    teachers = grade_class_teacher.objects.all()
    if request.method == 'POST':
        form = gradeClassTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            tcr = form.cleaned_data.get('teacher')
            grd = form.cleaned_data.get('grade_section')
            messages.success(request, f' {tcr} set as class teacher of {grd}')
            return redirect('add-class-teacher')
    else:
        form = gradeClassTeacherForm()
    return render(request, 'lead/add_classTeacher.html', {'form': form, 'title': 'Class Teacher', 'teachers': teachers})



class StudentListView(LoginRequiredMixin, ListView):
    model = student_details
    template_name = 'lead/student_details_listview.html'
    context_object_name = 'students'
    ordering = ['-id']


class TeacherListView(LoginRequiredMixin, ListView):
    model = teacher_details
    template_name = 'lead/teacher_details_listview.html'
    context_object_name = 'teachers'

class allbusListView(LoginRequiredMixin, ListView):
    model = bus_master
    template_name = 'lead/all-bus.html'
    context_object_name = 'transports'



class gradeTeacherUpdateView(LoginRequiredMixin, UpdateView ):
    model = grade_class_teacher
    fields = ['grade_section', 'teacher']
    template_name = 'lead/update_classteacher.html'



class teacherdetailUpdateView(LoginRequiredMixin, UpdateView):
    model = teacher_details
    fields = [
        'first_name',
        'last_name',
        'emp_code',
        'gender',
        'email',
        'mobile',
        'adress',
        'adress2',
        'pincode',
        'city',
        'state',
        'date_of_joining'
    ]
    template_name = 'lead/update_teacherdetails.html'





class busdetailsUpdateView(LoginRequiredMixin, UpdateView):
    model = bus_master
    fields = ['bus_reg_number', 'owner_mobile', 'owner_name', 'status']
    template_name = 'lead/update-bus.html'



def test(request):
    return render(request, 'lead/home.html')