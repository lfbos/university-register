from rest_framework import routers

from app.api import views

router = routers.DefaultRouter()

router.register(r'universities', views.UniversityViewSet, base_name='universities')
router.register(r'students', views.StudentViewSet, base_name='students')
router.register(r'professors', views.ProfessorViewSet, base_name='professors')
