from rest_framework import routers

from app.api.views import UniversityViewSet, StudentViewSet

router = routers.DefaultRouter()
# Register views

router.register(r'universities', UniversityViewSet, base_name='universities')
router.register(r'students', StudentViewSet, base_name='students')
