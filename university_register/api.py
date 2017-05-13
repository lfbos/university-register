from rest_framework import routers

from app.api.views import UniversityViewSet

router = routers.DefaultRouter()
# Register views

router.register(r'universities', UniversityViewSet, base_name='universities')
