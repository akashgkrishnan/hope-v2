from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import planners, teacher_details

# Create your views here.


def teacher_home(request):
    context = {}
    return render(request, 'teacher/teacher-index.html', context)


class PlannersCreateView(LoginRequiredMixin, CreateView):
    model = planners
    fields = ['title', 'content', 'approver']
    template_name = 'teacher/planners.html'

    def form_valid(self, form):
        teacher = teacher_details.objects.filter(user_name=self.request.user)[0]
        form.instance.author = teacher
        return super().form_valid(form)
