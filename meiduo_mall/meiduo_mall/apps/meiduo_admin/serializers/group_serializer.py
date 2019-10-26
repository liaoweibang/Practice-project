
from rest_framework import serializers
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',

            # 当前分组，所拥有对权限
            # 新建分组的时候，前端会传来一个列表: [1,2,3,4]
            'permissions',
        ]


    # def create(self, validated_data):
    #     # 反序列化新建分组的时候，构建中间表数据
    #
    #     # permissions = [1,2,3,4]
    #     # 1、从前端传来的数据中，提取中间表信息
    #     perm_list = validated_data.pop("permissions")
    #     # 2、创建分组对象: pk:19
    #     instance = Group.objects.create(**validated_data)
    #     # 3、创建中间表数据
    #     # instance.permissions = [1,2,3,4]
    #     instance.permissions.set(perm_list) # set([77])
    #
    #     return instance














