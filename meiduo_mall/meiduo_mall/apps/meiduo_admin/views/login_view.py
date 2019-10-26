
from rest_framework.views import APIView
from rest_framework.response import Response
from meiduo_admin.serializers.login_serializer import *

# 定义登陆视图，使用序列化器完成，响应请求

class LoginView(APIView):

    def post(self, reqeust):
        # 1、构建序列化器，传入前端浏览的参数，进行校验
        s = LoginSerializer(data=reqeust.data)
        s.is_valid(raise_exception=True)
        # 2、得到有效数据，构建响应对象
        return Response({
            "username": s.validated_data['user'].username,
            "user_id": s.validated_data['user'].id,
            "token": s.validated_data['token'],
        })
