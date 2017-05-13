from rest_framework import serializers

from app.models import University, Student, Course, Professor


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name',
                  'dni', 'university',)


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('first_name', 'last_name',
                  'dni', 'profession', 'university',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'professor')


class AssignCoursesSerializer(serializers.Serializer):
    student = serializers.ChoiceField(
        choices=Student.objects.all()
    )
    courses = serializers.MultipleChoiceField(
        choices=Course.objects.all(),
        allow_empty=False
    )
