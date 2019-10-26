

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from goods.models import SPU,Brand,GoodsCategory
from meiduo_admin.serializers.spu_serializer import *
from meiduo_admin.pages import MyPage
from rest_framework.response import Response


class SPUViewSet(ModelViewSet):
    queryset = SPU.objects.all().order_by('pk')
    serializer_class = SPUModelSerializer
    pagination_class = MyPage


    def get_queryset(self):
        # 如果一个请求。处理的视图方法是"spu_brands"
        # 那么，返回的数据集是Brand的查询集

        # self.action: 指的就是处理当前请求的视图方法的名称
        if self.action == "spu_brands":
            return Brand.objects.all()

        return self.queryset.all()


    def get_serializer_class(self):
        # 如果一个请求。处理的视图方法是"spu_brands"
        # 那么。返回的用于处理数据集的序列化器类SPUBrandSimpleSerializer
        if self.action == 'spu_brands':
            return SPUBrandSimpleSerializer
        return self.serializer_class


    def spu_brands(self, request):
        # 序列化返回所有品牌信息
        # 1、获得品牌数据对象查询集

        # 获得的是"Brand"模型类的查询集
        brand_queryset = self.get_queryset()
        # 2、获得序列化器对象
        s = self.get_serializer(brand_queryset, many=True)

        # 3、序列化返回
        return Response(s.data)





class SPUCategoryView(ListAPIView):
    # 一级分类：当前视图集默认处理的查询及是一级分类
    # queryset = GoodsCategory.objects.filter(parent=None)

    queryset = GoodsCategory.objects.all()
    serializer_class = SPUCategorySimpleSerializer


    def get_queryset(self):
        # 如果请求路径中，有pk，需要根据这个pk去过滤出二级或三级分类
        p_id = self.kwargs.get('pk')
        if p_id:
            # 返回二级或三级分类
            return self.queryset.filter(parent_id=p_id)

        # 返回一级分类
        return self.queryset.filter(parent=None)










