from rest_framework import viewsets

from .serializers import UsersSerializer
from .models import Users

# ModelViewSet handles GET & POST routes for Users
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('username')
    serializer_class = UsersSerializer