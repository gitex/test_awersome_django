from django.urls import path, include

from rest_framework import routers

from .users.views import UserViewSet, UserTableView


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('tables/users/', UserTableView.as_view()),
]
