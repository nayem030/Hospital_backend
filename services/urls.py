from rest_framework. routers import DefaultRouter
from django.urls import path, include
from .import views
 
router = DefaultRouter() # Amader Router 

router.register('services', views.ServicesViewSet)
urlpatterns = [
    path('', include(router.urls)),
]