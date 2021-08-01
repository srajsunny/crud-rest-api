
from crudapp.api.serializers import UserSerializer
from crudapp.models import User
from rest_framework import viewsets


class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class= UserSerializer
