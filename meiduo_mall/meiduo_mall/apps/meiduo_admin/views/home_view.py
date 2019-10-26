
from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from users.models import User
from orders.models import OrderInfo
from goods.models import GoodsVisitCount
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
import pytz
from meiduo_admin.serializers.home_serializer import *
from rest_framework.permissions import IsAdminUser

class HomeView(ViewSet):
    permission_classes = [IsAdminUser]

    # 用户总数
    # GET
    # statistical/total_count/
    @action(methods=['get'], detail=False)
    def total_count(self, request):
        # 1、统计用户总数
        count = User.objects.all().count()

        # timezone.now() --> 获得的是"当前的时间点"（是0时区的时间）
        # 0时区：2019-8-29  21：00：00
        # 上海： 2019-8-30  5：00：00
        shanghai_tz = pytz.timezone(settings.TIME_ZONE)
        shanghai_now_time = timezone.now().astimezone(tz=shanghai_tz)
        date = shanghai_now_time.date()

        # 2、构建响应数据
        return Response({
            "count": count,
            "date": date
        })

    # 日增用户
    # GET
    # statistical/day_increment/
    @action(methods=['get'], detail=False)
    def day_increment(self, request):
        # 统计当日新增用户，过滤出用户创建时间大于等于"今日"的零时
        # 1、获得"当日"的零时
        cur_time_0 = timezone.now()
        cur_shanghai = cur_time_0.astimezone(pytz.timezone(settings.TIME_ZONE))
        # 2019-8-30 0:0:0
        shanghai_0 = cur_shanghai.replace(hour=0, minute=0, second=0)

        # 2、过滤用户数
        count = User.objects.filter(date_joined__gte=shanghai_0).count()

        return Response({
            "count": count,
            "date": shanghai_0.date()
        })

    # 日活跃用户
    # GET
    # statistical/day_active/
    @action(methods=['get'], detail=False)
    def day_active(self, request):
        # 1、获得当日零时
        cur_0_time = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).\
            replace(hour=0, minute=0, second=0, microsecond=0)
        # 2、过滤，统计用户数量
        count = User.objects.filter(last_login__gte=cur_0_time).count()
        # 3、构建响应数据
        return Response({
            'count': count,
            'date': cur_0_time.date()
        })


    # 日下单用户数量
    # GET
    # statistical/day_orders/
    @action(methods=['get'], detail=False)
    def day_orders(self, request):
        # 统计 "当日" 下单的 用户
        # 1、已知条件：当日的零时
        # 2、目标数据：用户
        # 思考：已知条件是从表，查询目标数据是主表

        # # 方案一：从从表入手
        # # 1、根据已知条件，查询从表数据对象
        # cur_0_time = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)). \
        #     replace(hour=0, minute=0, second=0, microsecond=0)
        # order_list = OrderInfo.objects.filter(create_time__gte=cur_0_time)
        #
        # # 2、从这些订单中找出用户
        # user_list = []
        # for order in order_list:
        #     # order: 每一个订单对象
        #     user_list.append(order.user)
        # # 3、user_list列表。保存的就是所有订单关联用户（可能存在重复）
        # # 去重,统计当日下单用户数量
        # count = len(set(user_list))
        #
        # # 4、构建响应
        # return Response({
        #     'count': count,
        #     'date': cur_0_time.date()
        # })

        # 方案二：从主表入手

        cur_0_time = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)). \
                    replace(hour=0, minute=0, second=0, microsecond=0)

        user_list = User.objects.filter(orders__create_time__gte=cur_0_time)
        count = len(set(user_list))

        return Response({
            'count': count,
            'date': cur_0_time.date()
        })

    # 月新增用户统计（30天）
    # GET
    # statistical/month_increment/
    @action(methods=['get'], detail=False)
    def month_increment(self, request):
        # 1、当日零时（终止时间点）
        # 2019-8-30 0:0:0
        cur_0_time = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)). \
            replace(hour=0, minute=0, second=0, microsecond=0)
        # 2、启始时间点
        # 2019-8-1 0:0:0
        start_0_time = cur_0_time - timedelta(days=29)

        # 3、启始时间点(零时) 到 当日零时 之间每一天新增到用户
        user_list = []
        for index in range(30):
            # index:        0                                   1
            # calc_0_time:  start_0_time+timedelta(days=0)    start_0_time+timedelta(days=1)
            # 用于计算的某一天的0时
            calc_0_time = start_0_time + timedelta(days=index)
            next_0_time = calc_0_time + timedelta(days=1)
            count = User.objects.filter(date_joined__gte=calc_0_time, date_joined__lt=next_0_time).count()

            user_list.append({
                'count': count,
                'date': calc_0_time.date()
            })
        # 4、构建返回数据
        return Response(user_list)



# 序列化返回GoodsVisitCount多条数据
class GoodsVisitCountView(ListAPIView):
    queryset = GoodsVisitCount.objects.all()
    serializer_class = GoodsVisitCountSerializer

    permission_classes = [IsAdminUser]

    def get_queryset(self):
        cur_0_time = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)). \
            replace(hour=0, minute=0, second=0, microsecond=0)
        return self.queryset.filter(create_time__gte=cur_0_time)














