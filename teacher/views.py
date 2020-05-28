from datetime import date

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, ListView

from .models import planners, teacher_details, teacher_subject_grade_section, grade_class_teacher
from student.models import student_details, attendance_history, student_attendance
# Create your views here.


def teacher_home(request):
    teacher = teacher_details.objects.filter(user_name=request.user)[0]
    if grade_class_teacher.objects.filter(teacher=teacher).exists():
        is_classTeacher = True
    else:
        is_classTeacher = False

    teacher_subjects = teacher_subject_grade_section.objects.filter(
        teacher=teacher)
    context = {
        "my_subjects": teacher_subjects,
        'is_classTeacher': is_classTeacher,
        'teacher': teacher
    }
    return render(request, 'teacher/teacher-index.html', context)


class PlannersCreateView(LoginRequiredMixin, CreateView):
    model = planners
    fields = ['title', 'content', 'approver']
    template_name = 'teacher/planners.html'

    def form_valid(self, form):
        teacher = teacher_details.objects.filter(
            user_name=self.request.user)[0]

        form.instance.author = teacher
        return super().form_valid(form)


def my_planners(request):
    teacher = teacher_details.objects.filter(user_name=request.user)[0]
    my_planners = planners.objects.filter(author=teacher)
    context = {
        'my_planners': my_planners
    }
    return render(request, 'teacher/my-planners.html', context)


def planners_Detail(request, pk):
    my_planners = planners.objects.get(id=pk)
    context = {
        'planner': my_planners
    }
    return render(request, 'teacher/my_planner_Detail.html', context)


@login_required
def student_gradelist(request, pk):
    students = student_details.objects.filter(grade_section=pk)
    context = {'students': students}
    return render(request, 'teacher/studentGrade_listView.html', context)

@login_required
def student_DetailView(request, pk):
    student = student_details.objects.get(id = pk)
    context = {
        'student': student
    }
    return render(request, 'teacher/student_detailView.html', context)


@login_required
def attendance(request):
    user = teacher_details.objects.get(user_name = request.user)
    grade_ct = grade_class_teacher.objects.get(teacher = user)
    students = student_details.objects.filter(grade_section=grade_ct.grade_section)
    today = date.today()
    if request.method == 'POST':
        if attendance_history.objects.filter(attendance_of=grade_ct).filter(attended_on=today).exists():
            messages.warning(request, f'you have already marked todays attendance')
            return redirect('teacher-home')    
        else:
            for student in students:
                val = 'student'+str(student.id)
                attend = request.POST.get(val)
                new = student_attendance(student=student, attended=attend, date=today)
                new.save()
            new_history = attendance_history(attendance_of = grade_ct, attended_on = today)
            new_history.save()
        return redirect('teacher-home')

    return render(request, 'teacher/attendance.html', {'students': students, 'date': today})