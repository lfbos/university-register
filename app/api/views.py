from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from app.api.serializers import (
    UniversitySerializer,
    StudentSerializer,
    ProfessorSerializer,
    AssignCoursesSerializer,
    CourseSerializer
)
from app.models import University, Student, Professor, Course


class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class ProfessorViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class AssignCoursesViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = AssignCoursesSerializer
    queryset = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student = serializer.validated_data.get('student')
        courses = serializer.validated_data.get('courses')

        if all(
            student.university == course.professor.university
            for course in courses
        ):
            student.courses = courses
            student.save()

            return Response({'message': 'Courses assigned successfully'},
                            status=status.HTTP_200_OK)

        else:
            return Response(
                {'error': 'Error! The courses must be from the same university'},
                status=status.HTTP_400_BAD_REQUEST
            )
