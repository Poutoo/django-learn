from rest_framework import viewsets
from .models import Dragon
from .serializers import DragonSerializer

class DragonViewSet(viewsets.ModelViewSet):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer
