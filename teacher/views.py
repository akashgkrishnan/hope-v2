from django.shortcuts import render

# Create your views here.

def teacher_home(request):
    context = {}
    return render(request, 'teacher/teacher-index.html', context)