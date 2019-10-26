
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SKU,GoodsCategory,SPUSpecification
from meiduo_admin.serializers.sku_serializer import *
from meiduo_admin.pages import MyPage

class SKUViewSet(ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKUModelSerializer
    pagination_class = MyPage


    def get_queryset(self):
        keyword = self.request.query_params.get("keyword")
        if keyword:
            return self.queryset.filter(name__contains=keyword)

        return self.queryset.all()



class GoodsCategoryView(ListAPIView):
    queryset = GoodsCategory.objects.filter(parent_id__gt=37)
    serializer_class = GoodsCategorySimpleSerializer



class SPUSimpleView(ListAPIView):
    queryset = SPU.objects.all()
    serializer_class = SPUSimpleSerializer


class SPUSpecOptView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecSerializer

    def get_queryset(self):
        # 1、提取前端传来的spu_id
        spu_id = self.kwargs.get("pk")
        # 2、过滤出关联spu_id的所有的SPUSpecification对象
        # 3、返回过滤后的数据集
        return self.queryset.filter(spu_id=spu_id)



# from rest_framework.views import APIView
# class HelloView(APIView):
#     # GET
#     # /hello/(?P<name>\w+)/
#     def get(self, request, age, name):
#         print("name: ", name)
#         print("age: ", age)
#         return Response({"result":"OK"})










