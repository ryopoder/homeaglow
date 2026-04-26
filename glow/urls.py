# from django.urls import path, include
# # from django.contrib.auth.models import User
# from glow.models import User
# from rest_framework import routers, serializers, viewsets
#
#
# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["url", "username", "email", "is_staff"]
#
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r"users", UserViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path("", include(router.urls)),
#     path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from glow import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"rooms", views.RoomViewSet, basename="room")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", views.home, name="home"),
    path("room-info/", views.room_info, name="room_info"),
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]