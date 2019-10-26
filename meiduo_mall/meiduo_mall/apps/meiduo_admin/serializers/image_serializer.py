

from rest_framework import serializers
from goods.models import SKUImage,SKU
from meiduo_mall.utils.fdfs.storage import fdfs_send_filebuffer


class ImageModelSerializer(serializers.ModelSerializer):

    # 可以作用于：序列化成管理主表对象的id
    # 也可以作用于：反序列化传入的值也是管理主表的id
    # 注意事项：如果PrimaryKeyRelatedField作用于反序列化，那么必须通过queryset约束条件
    #         指明管理的主表的对象查询集合
    #         反序列化行为：需要给他一个主表对象的id，接着会根据这个id，在queryset约束条件中过滤出主表关联对象
    #          SKU.objects.create(sku=queryset.filter(pk=19))
    # sku = PrimaryKeyRelatedField(queryset=SKU.objects.all())
    class Meta:
        model = SKUImage
        fields = [
            'id',
            'sku',
            'image'
        ]


    # def validate_image(self, value):
    #     """
    #     :param value: 经过前序校验的当前字段的值，是一个文件对象
    #     :return:
    #     """
    #     pass


    # def validate(self, attrs):
    #     # 上传fdfs文件
    #     # 1、获得文件对象
    #     file_obj = attrs.pop('image')
    #     # 2、读取文件内容
    #     content = file_obj.read()
    #     # 3、使用fdfs客户端完成上传
    #     res = fdfs_send_filebuffer(content)
    #     # 4、新建图片数据
    #     if res['Status'] != "Upload successed.":
    #         raise serializers.ValidationError("上传失败")
    #
    #     attrs['image'] = res['Remote file_id']
    #     return attrs


    # def create(self, validated_data):
    #     # 上传fdfs文件
    #     # 1、获得文件对象
    #     file_obj = validated_data.pop('image')
    #     # 2、读取文件内容
    #     content = file_obj.read()
    #     # 3、使用fdfs客户端完成上传
    #     res = fdfs_send_filebuffer(content)
    #     # 4、新建图片数据
    #     if not res['Status'] == "Upload successed.":
    #         raise serializers.ValidationError("上传失败")
    #
    #     validated_data['image'] = res['Remote file_id']
    #     return super().create(validated_data)
    #
    #
    # def update(self, instance, validated_data):
    #     # 上传fdfs文件
    #     # 1、获得文件对象
    #     file_obj = validated_data.pop('image')
    #     # 2、读取文件内容
    #     content = file_obj.read()
    #     # 3、使用fdfs客户端完成上传
    #     res = fdfs_send_filebuffer(content)
    #     # 4、新建图片数据
    #     if not res['Status'] == "Upload successed.":
    #         raise serializers.ValidationError("上传失败")
    #
    #     validated_data['image'] = res['Remote file_id']
    #     return super().update(instance, validated_data)



class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['id', 'name']
