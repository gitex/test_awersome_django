from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
import django_tables2 as tables

from core.apps.users.models import User
from core.apps.users.tables import UserTable

from .serializers import UserSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTableView(tables.SingleTableView):
    table_class = UserTable
    queryset = User.objects.all()
    template_name = "django_tables2/bootstrap.html"
