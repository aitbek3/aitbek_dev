from django.urls import path
from .views import *

urlpatterns = [
    path('userprofileprofessor', UserProfileProfessorListViewSets.as_view(),
         name='userprofileprofessor_list'),

    path('userprofileprofessor/<int:pk>/', UserProfileProfessorListViewSets.as_view(),
         name='userprofileprofessor_detail'),

    path('userprofilestudent', UserProfileStudentListViewSets.as_view(),
         name='userprofilestudent_list'),

    path('userprofilestudent/<int:pk>/', UserProfileStudentListViewSets.as_view(),
         name='userprofilestudent_detail'),

    path('faculty', FacultyListViewSets.as_view(),
         name='faculty_list'),

    path('faculty/<int:pk>/', FacultyListViewSets.as_view(),
         name='faculty_detail'),

    path('professor', ProfessorListViewSets.as_view(),
         name='professor_list'),

    path('professor/<int:pk>/', ProfessorListViewSets.as_view(),
         name='professor_detail'),

    path('student', StudentListViewSets.as_view(),
         name='student_list'),

    path('student/<int:pk>/', StudentListViewSets.as_view(),
         name='student_detail'),

    # path('course', CourseListViewSets.as_view(),
    #      name='course_list'),
    #
    # path('course/<int:pk>/', CourseListViewSets.as_view(),
    #      name='course_detail'),

    path('room', RoomListViewSets.as_view(),
         name='room_list'),

    path('room/<int:pk>/', RoomListViewSets.as_view(),
         name='room_detail'),

    path('schedule', ScheduleListViewSets.as_view(),
         name='schedule_list'),

    path('schedule/<int:pk>/', ScheduleListViewSets.as_view(),
         name='schedule_detail'),

    path('registration', RegistrationListViewSets.as_view(),
         name='registration_list'),

    path('registration/<int:pk>/', RegistrationListViewSets.as_view(),
         name='registration_detail'),

    path('homework', HomeworkListViewSets.as_view(),
         name='homework_list'),

    path('homework/<int:pk>/', HomeworkListViewSets.as_view(),
         name='homework_detail'),

    path('submitting', SubmittingListViewSets.as_view(),
         name='submittinglist'),

    path('submitting/<int:pk>/', SubmittingListViewSets.as_view(),
         name='submitting_detail'),

]