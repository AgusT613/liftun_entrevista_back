from .models import EnvironmentAction
from .serializers import EnvironmentActionSerializer
from rest_framework import viewsets


class EnvironmentActionViewSet(viewsets.ModelViewSet):
    queryset = EnvironmentAction.objects.all()
    serializer_class = EnvironmentActionSerializer
