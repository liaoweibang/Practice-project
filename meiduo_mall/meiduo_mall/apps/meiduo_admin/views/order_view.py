

from rest_framework.mixins import ListModelMixin
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.generics import GenericAPIView
from orders.models import OrderInfo
from meiduo_admin.serializers.order_serializer import *
from meiduo_admin.pages import MyPage
from rest_framework.permissions import BasePermission


class MyAddOrderInfo(BasePermission):
    """
    # 自定义权限，有没有对OrderInfo这张表对"增加"和"修改"权限
    """
    def has_permission(self, request, view):
        return request.user and request.user.has_perm("users.chifan")
        # return request.user and request.user.has_perms(["orders.add_orderinfo", "orders.change_orderinfo"])


class OrderInfoView(ListAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoModelSerializer
    pagination_class = MyPage

    # permission_classes = [MyAddOrderInfo]

    def get_queryset(self):
        # 实现根据keyword过滤order_id
        keyword = self.request.query_params.get("keyword")
        if keyword is not None:
            return self.queryset.filter(order_id__contains=keyword)
        return self.queryset.all()


class OrderInfoDetailView(RetrieveAPIView, UpdateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoDetailSerializer
