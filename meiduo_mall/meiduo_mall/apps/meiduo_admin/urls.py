from django.conf.urls import url
from meiduo_admin.views.login_view import LoginView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter
from meiduo_admin.views.home_view import *
from meiduo_admin.views.user_view import *
from meiduo_admin.views.sku_view import *
from meiduo_admin.views.spu_view import *
from meiduo_admin.views.spec_view import *
from meiduo_admin.views.option_view import *
from meiduo_admin.views.channel_view import *
from meiduo_admin.views.brands_view import *
from meiduo_admin.views.image_view import *
from meiduo_admin.views.order_view import *
from meiduo_admin.views.perm_view import *
from meiduo_admin.views.group_view import *
from meiduo_admin.views.admin_view import *

urlpatterns = [
    # 用户登陆接口
    # url(r'authorizations/', LoginView.as_view()),
    url(r'authorizations/', obtain_jwt_token),

    # 日分类访问量
    url(r'statistical/goods_day_views/', GoodsVisitCountView.as_view()),

    # 主页url
    # 1、用户总数统计
    # url(r'statistical/total_count/', HomeView.as_view({"get":"total_count"}))

    # 序列化返回多个超级管理员用户对象
    url(r'^users/$', UserAPIView.as_view()),

    # SKU表管理
    url(r'^skus/$', SKUViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^skus/(?P<pk>\d+)/$', SKUViewSet.as_view({"get":"retrieve",
                                                    "delete":"destroy",
                                                    "put":"update"})),
    # 获得新建sku可选三级分类
    url(r'^skus/categories/$', GoodsCategoryView.as_view()),
    # 获得新建sku可选spu
    url(r'^goods/simple/$', SPUSimpleView.as_view()),
    # 获得spu可选规格及选项信息
    url(r'^goods/(?P<pk>\d+)/specs/$', SPUSpecOptView.as_view()),

    # spu管理
    # url(r'^goods/$', SPUViewSet.as_view({"get":"list", "post":"create"})),
    # url(r'^goods/(?P<pk>\d+)/$', SPUViewSet.as_view({"get":"retrieve",
    #                                                  "put":"update",
    #                                                  "delete":"destroy"})),

    # 获得新增spu可选品牌信息
    url(r'^goods/brands/simple/$', SPUViewSet.as_view({"get":"spu_brands"})),
    # 获得新增spu可选一级分类信息
    url(r'^goods/channel/categories/$', SPUCategoryView.as_view()),
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', SPUCategoryView.as_view()),


    # 选项表管理
    # 1、序列化返回多条数据：  get --> list
    # 2、校验前端说数据，根据有效数据新建对象： post -->  create
    url(r'^specs/options/$', OptViewSet.as_view({"get":"list", "post":"create"})),
    # 3、根据路径唯一过滤条件(默认是pk)，过滤出单一对象并序列化返回： get --> retrieve
    # 4、根据路径唯一过滤条件(默认是pk)，过滤出单一对象并更新： put --> update
    # 5、根据路径唯一过滤条件(默认是pk)，过滤出单一对象并删除： delete --> destroy
    url(r'^specs/options/(?P<pk>\d+)/$', OptViewSet.as_view({"get":"retrieve",
                                                             "put":"update",
                                                             "delete":"destroy"})),


    # 获得新增选项可选规格信息
    url(r'^goods/specs/simple/$', OptSpecView.as_view()),

    # 频道管理
    url(r'^goods/channels/$', ChannelViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^goods/channels/(?P<pk>\d+)/$', ChannelViewSet.as_view({"delete":"destroy",
                                                                  "get":"retrieve",
                                                                  "put":"update"})),

    # 新建频道可选一级分类信息
    url(r'^goods/categories/$', SPUCategoryView.as_view()),
    # 新建频道可选分组信息
    url(r'^goods/channel_types/$', ChannelGroupView.as_view()),


    # url(r'^hello/(?P<name>\w+)/(\d+)/$', HelloView.as_view())
    # url(r'^hello/(\w+)/(\d+)/$', HelloView.as_view())

    # 品牌表管理
    url(r'^goods/brands/$', BrandViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^goods/brands/(?P<pk>\d+)/$', BrandViewSet.as_view({"get":"retrieve",
                                                              "put":"update",
                                                              "delete":"destroy"})),

    # 图片管理
    url(r'^skus/images/$', ImageViewSet.as_view({"get":"list","post":"create"})),
    url(r'^skus/images/(?P<pk>\d+)/$', ImageViewSet.as_view({"get":"retrieve",
                                                             "put":"update",
                                                             "delete":"destroy"})),

    # 新增图片可选skus
    url(r'^skus/simple/$', ImageViewSet.as_view({"get":"get_skus"})),

    # 订单管理
    url(r'^orders/$', OrderInfoView.as_view()),
    url(r'^orders/(?P<pk>\d+)/$', OrderInfoDetailView.as_view()),
    # 修改订单状态
    url(r'^orders/(?P<pk>\d+)/status/$', OrderInfoDetailView.as_view()),

    # 权限管理
    url(r'^permission/perms/$', PermViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^permission/perms/(?P<pk>\d+)/$', PermViewSet.as_view({"get":"retrieve",
                                                                 "put":"update",
                                                                 "delete":"destroy"})),

    # 新增权限可选类型
    url(r'^permission/content_types/$', PermTypeView.as_view()),

    # 分组管理
    url(r'^permission/groups/$', GroupViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^permission/groups/(?P<pk>\d+)/$', GroupViewSet.as_view({"delete":"destroy",
                                                                   "get":"retrieve",
                                                                   "put":"update"})),

    # 新增分组可选权限
    url(r'^permission/simple/$', PermSimpleView.as_view()),


    # 管理员管理
    url(r'^permission/admins/$', AdminViewSet.as_view({"get":"list", "post":"create"})),
    url(r'^permission/admins/(?P<pk>\d+)/$', AdminViewSet.as_view({"get":"retrieve",
                                                                   "put":"update",
                                                                   "delete":"destroy"})),


    # 新建管理员可选分组信息
    url(r'^permission/groups/simple/$', AdminGroupSimpleView.as_view()),
]


# 1、路由对象，只需要有一个
# 2、可以使用该对象，多次对不同视图集进行注册

router = SimpleRouter()
router.register(prefix='statistical', viewset=HomeView, base_name="home")

# 视图集中list方法对应自动构建对路径是： url(r'goods/specs/$', SpecViewSet.as_view({"get":"list"))
# 视图集中create方法对应自动构建对路径是： url(r'goods/specs/$', SpecViewSet.as_view({"get":"list", "post":"create"))
# 视图集中retrieve方法对应自动构建对路径是： url(r'goods/specs/(?P<pk>[^/.]+)/$', SpecViewSet.as_view({"get":"retrieve"))
# 视图集中update方法对应自动构建对路径是： url(r'goods/specs/(?P<pk>[^/.]+)/$', SpecViewSet.as_view({"get":"retrieve", "put":"update"))
# 视图集中destroy方法对应自动构建对路径是： url(r'goods/specs/(?P<pk>[^/.]+)/$', SpecViewSet.as_view({"get":"retrieve", "put":"update", "delete":"destroy"))
# 注意事项：prefix前缀，定义的时候，前后不要有'/'
router.register(prefix='goods/specs', viewset=SpecViewSet, base_name='spec')

# 把SPU管理路径放在Sec之后注册，目的在于避免屏蔽效应
# goods/(?P<pk>[^/.]+)/  屏蔽了  goods/specs/
router.register(prefix='goods', viewset=SPUViewSet, base_name='spu')
urlpatterns += router.urls





















