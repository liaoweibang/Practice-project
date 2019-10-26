
from rest_framework import serializers
from goods.models import SPU,Brand,GoodsCategory


class SPUModelSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField() # read_only=True
    brand_id = serializers.IntegerField()
    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        # fields = "__all__"
        exclude = ['category1', 'category2', 'category3'] # 字段剔除

        # extra_kwargs = {
        #     "category1": {'read_only':True}
        # }



class SPUBrandSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']



class SPUCategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['id',  'name']