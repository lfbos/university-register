from rest_framework import serializers

from app.models import University, Student, Course, Professor


class UniversitySerializer(serializers.ModelSerializer):
    pk = serializers.CharField(read_only=True)

    class Meta:
        model = University
        fields = ('pk', 'name',)


class StudentSerializer(serializers.ModelSerializer):
    pk = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ('pk', 'first_name', 'last_name',
                  'dni', 'university',)


class ProfessorSerializer(serializers.ModelSerializer):
    pk = serializers.CharField(read_only=True)

    class Meta:
        model = Professor
        fields = ('pk', 'first_name', 'last_name',
                  'dni', 'profession', 'university',)


class CourseSerializer(serializers.ModelSerializer):
    pk = serializers.CharField(read_only=True)

    class Meta:
        model = Course
        fields = ('pk', 'name', 'professor')


class AssignCoursesSerializer(serializers.Serializer):
    student = serializers.ChoiceField(
        choices=Student.objects.all()
    )
    courses = serializers.MultipleChoiceField(
        choices=Course.objects.all(),
        allow_empty=False
    )
