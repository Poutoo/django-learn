from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DragonViewSet

router = DefaultRouter()
router.register(r'dragons', DragonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
