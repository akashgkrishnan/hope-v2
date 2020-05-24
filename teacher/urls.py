from django.urls import path
from . import views


urlpatterns = [
    path('teacher-home', views.teacher_home, name='teacher-home'),
    path('planners', views.PlannersCreateView.as_view(), name='planners'),
    path('my-planners', views.my_planners,name='my-planners' ),
    path('my-planner-details/<str:pk>', views.planners_Detail, name='my-planner-details')
]