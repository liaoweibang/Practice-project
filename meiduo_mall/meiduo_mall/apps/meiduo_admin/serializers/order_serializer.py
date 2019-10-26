

from rest_framework import serializers
from orders.models import OrderInfo,OrderGoods
from goods.models import SKU


class OrderInfoModelSerializer(serializers.ModelSerializer):
    # create_time = serializers.DateTimeField(format="%Y/%m/%d")# , input_formats="%Y/%m/%d")

    class Meta:
        model = OrderInfo
        fields = ['order_id', 'create_time']

        extra_kwargs = {
            "create_time": {"format": "%Y/%m/%d"}
        }


class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = [
            'name',
            'default_image'
        ]


class OrderGoodsSerializer(serializers.ModelSerializer):

    # SKU模型类对象（单一主表对象）
    sku = SKUSimpleSerializer()
    class Meta:
        model = OrderGoods
        fields = [
            'count',
            'price',
            'sku'
        ]


class OrderInfoDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    # 当前订单OrderInfo对象，关联的订单商品OrderGoods表所有对象数据集
    skus = OrderGoodsSerializer(many=True)
    class Meta:
        model = OrderInfo
        fields = "__all__"