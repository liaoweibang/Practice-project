
from rest_framework.generics import ListAPIView,CreateAPIView
from users.models import User
from meiduo_admin.serializers.user_serializer import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from meiduo_admin.pages import MyPage


class UserAPIView(ListAPIView, CreateAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserModelSerializer

    pagination_class = MyPage

    def get_queryset(self):
        """
        后续所有的序列化处理的数据集
        都是通过该函数获得的
        我只要重写该函数，就可以控制，处理的视图集
        """
        # 如果字符串参数中，有keyword，那么就应该
        # 根据self.queryset.filter(username__contains=keyword)

        # 请求对象就是：视图对象.request
        keyword = self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(username__contains=keyword)
        # self.queryset.all()的目的：获得最新的数据
        return self.queryset.all()