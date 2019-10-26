

from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'mobile',
                  'email',

                  'password'
                  ]

        extra_kwargs = {
            "password": {"write_only": True}
        }


    def validate(self, attrs):
        # 1、attrs数据中缺少了is_staff=True
        # 2、attrs数据中的密码是明文的

        attrs['is_staff'] = True
        attrs['password'] = make_password(attrs['password'])

        return attrs


    # def create(self, validated_data):
    #     # validated_data = {"username":xx, ....}
    #
    #     # 1、有效数据中的密码是明文的
    #     # 2、有效数据中，没有is_staff=True
    #     # return User.objects.create(**validated_data)
    #
    #     # 创建超级管理员，自动地加密明文密码
    #     return User.objects.create_superuser(**validated_data)















