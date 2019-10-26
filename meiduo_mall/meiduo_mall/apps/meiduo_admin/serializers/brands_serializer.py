

from rest_framework import serializers
from goods.models import Brand
from fdfs_client.client import Fdfs_client
from django.conf import settings
from meiduo_mall.utils.fdfs.storage import fdfs_send_filebuffer


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',

            # 当前logo是一个文件类型的字段，在反序列化的时候
            # 会将前端传来的文件数据，反序化组织成文件对象
            'logo',
            'first_letter'
        ]

    # 有效数据
    # name：品牌名称
    # first_letter： 首字母
    # logo：文件对象
    # def validate(self, attrs):
    #     # 上传fdfs文件
    #     # 1、获得文件对象
    #     file_obj = attrs.pop('logo')
    #     # 2、读取文件内容
    #     content = file_obj.read()
    #     # 3、使用fdfs客户端完成上传
    #     res = fdfs_send_filebuffer(content)
    #     # 4、新建图片数据
    #     if not res['Status'] == "Upload successed.":
    #         raise serializers.ValidationError("上传失败")
    #
    #     attrs['logo'] = res['Remote file_id']
    #     return attrs



    # def create(self, validated_data):
    #     """
    #     问题：无法完成数据上传fdfs的操作
    #     :param validated_data:
    #     :return:
    #     """
    #     # 1、获得文件数据
    #     # file_obj = open("文件", "rb")
    #     file_obj = validated_data.get("logo")
    #     # 提取数据
    #     content = file_obj.read()
    #     # 2、将该文件数据上传fdfs
    #     res = fdfs_send_filebuffer(content)
    #     # 3、上传成功则, 记录返回的文件id
    #     if not res['Status'] == "Upload successed.":
    #         raise serializers.ValidationError("上传失败")
    #
    #     # 4、构建模型类对象，保存数据库
    #
    #     # 修改logo字段。以在mysql中记录文件fdfs的id
    #     validated_data['logo'] = res['Remote file_id']
    #     return super().create(validated_data)
    #
    #
    # def update(self, instance, validated_data):
    #     """
    #     更新文件的上传操作
    #     :param instance:
    #     :param validated_data:
    #     :return:
    #     """
    #
    #     # 1、获得文件数据
    #     # file_obj = open("文件", "rb")
    #     file_obj = validated_data.get("logo")
    #     # 提取数据
    #     content = file_obj.read()
    #     # 2、将该文件数据上传fdfs
    #     res = fdfs_send_filebuffer(content)
    #     # 3、上传成功则, 记录返回的文件id
    #     if not res['Status'] == "Upload successed.":
    #         raise serializers.ValidationError("上传失败")
    #
    #     # 4、构建模型类对象，保存数据库
    #
    #     # 修改logo字段。以在mysql中记录文件fdfs的id
    #     validated_data['logo'] = res['Remote file_id']
    #
    #     return super().update(instance, validated_data)






