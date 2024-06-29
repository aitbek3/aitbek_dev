from rest_framework import generics, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegisterSerializer


class UserProfileProfessorListViewSets(generics.ListAPIView):
    queryset = UserProfileProfessor.objects.all()
    serializer_class = UserProfileProfessorSerializers
    permissions_classes = [permissions.IsAuthenticated]


class UserProfileProfessorDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfileProfessor.objects.all()
    serializer_class = UserProfileProfessorSerializers
    permission_classes = [permissions.IsAuthenticated]


class UserProfileStudentListViewSets(generics.ListAPIView):
    queryset = UserProfileStudent.objects.all()
    serializer_class = UserProfileStudentSerializers
    permission_classes = [permissions.IsAuthenticated]


class UserProfileStudentDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfileStudent.objects.all()
    serializer_class = UserProfileStudentSerializers
    permission_classes = [permissions.IsAuthenticated]


class FacultyListViewSets(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class FacultyDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers
    permission_classes = [permissions.IsAuthenticated]


class ProfessorListViewSets(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializers
    permission_classes = [permissions.IsAuthenticated]


class ProfessorDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializers
    permission_classes = [permissions.IsAuthenticated]


class StudentListViewSets(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]


class StudentDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]


# class CourseListViewSets(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializers
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# class CourseDetailMixins(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializers
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return None  # Возвращаем пустой queryset

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Создаем нового пользователя на основе валидированных данных
            return Response({
                "user": serializer.data,
                "message": "User created successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomListViewSets(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = [permissions.IsAuthenticated]


class RoomDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = [permissions.IsAuthenticated]


class ScheduleListViewSets(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializers
    permission_classes = [permissions.IsAuthenticated]


class ScheduleDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializers
    permission_classes = [permissions.IsAuthenticated]


class RegistrationListViewSets(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializers
    permission_classes = [permissions.IsAuthenticated]


class RegistrationDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializers
    permission_classes = [permissions.IsAuthenticated]


class HomeworkListViewSets(generics.ListAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializers
    permission_classes = [permissions.IsAuthenticated]


class HomeworkDetailMixins(generics.RetrieveDestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializers
    permission_classes = [permissions.IsAuthenticated]


class SubmittingListViewSets(generics.ListAPIView):
    queryset = Submitting.objects.all()
    serializer_class = SubmittingSerializers
    permission_classes = [permissions.IsAuthenticated]


class SubmittingDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submitting.objects.all()
    serializer_class = SubmittingSerializers
    permission_classes = [permissions.IsAuthenticated]



