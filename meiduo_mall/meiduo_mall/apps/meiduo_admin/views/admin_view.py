

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from users.models import User
from django.contrib.auth.models import Group
from meiduo_admin.serializers.admin_serializer import *
from meiduo_admin.serializers.group_serializer import GroupSerializer
from meiduo_admin.pages import MyPage


class AdminViewSet(ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer
    pagination_class = MyPage

class AdminGroupSimpleView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer