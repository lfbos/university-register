from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app.api.serializers import UniversitySerializer
from app.models import University


class UniversityViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
