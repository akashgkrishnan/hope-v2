from django.urls import path
from . import views


urlpatterns = [
    path('lead-home',views.lead_index, name='lead-home'),
    path('add-management', views.create_management, name='add-management'),
    path('add-leaduser', views.create_leaduser, name='add-leaduser'),
    path('add-bus', views.create_bus, name='add-bus'),
    path('add-event', views.events , name='add-event'),
    path('add-subject', views.subject_create, name='add-subject'),
    path('add-subject-section', views.subjectSection, name='add-subject-section'),
    path('add-student', views.add_student, name='add-student'),
    path('add-teacher', views.add_teacher, name='add-teacher'),
    path('add-subject-teacher', views.subject_teachers, name='add-subject-teacher'),
    path('add-class-teacher', views.add_classteacher, name='add-class-teacher'),
    path('add-tasks', views.create_todos, name='add-tasks'),
    path('delete-task/<str:pk>', views.delete_task, name='delete-task'),
    path('complete/<str:pk>', views.complete, name='complete'),
    path('departments', views.departments, name='departments'),
    path('all-student', views.StudentListView.as_view(), name='all-student'),
    path('all-teacher', views.TeacherListView.as_view(), name='all-teacher'),
    path('all-bus', views.allbusListView.as_view(), name='all-bus'),
    path('all-managers', views.ManagementListView.as_view(),name='all-managers'),
    path('all-admin', views.LeadListView.as_view(), name='all-admin'),
    path('update-cteacher/<str:pk>', views.gradeTeacherUpdateView.as_view(), name='update-cteacher'),
    path('update-teacher/<str:pk>', views.teacherdetailUpdateView.as_view(), name='update-teacher'),
    path('update-bus/<str:pk>', views.busdetailsUpdateView.as_view(), name='update-bus'),
    path('test', views.test, name='test')
]