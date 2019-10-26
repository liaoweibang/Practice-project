
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response



# 可不可以用于分页处理别的模型类数据集
class MyPage(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "pagesize"
    max_page_size = 10

    def get_paginated_response(self, data):
        """
        构建响应对象（封装响应的数据格式）
        :param data: 分页的子集序列化后的数据（字典）
        :return: 响应对象
        """
        return Response({
            "counts": self.page.paginator.count,
            "lists": data,
            "page": self.page.number,
            "pages": self.page.paginator.num_pages,
            "pagesize": self.page_size,
        })