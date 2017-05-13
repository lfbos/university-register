from rest_framework import viewsets

from app.api.serializers import UniversitySerializer, StudentSerializer
from app.models import University, Student


class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
