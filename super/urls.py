"""super URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
# from django.contrib import admin
from django.views.generic.base import TemplateView
import xadmin
from super.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewset
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
# from users.views import SmsCodeViewset,UserViewset
from users.views import UserViewset
from user_operation.views import UserFavViewset
from trade.views import ShoppingCartViewset, OrderViewset
# franmework的router在此注册
router = routers.DefaultRouter()

router.register(r'goods', GoodsListViewSet, base_name='goods')
# 配置分类url
router.register(r'categorys', CategoryViewset, base_name='categorys')
# router.register(r'code', SmsCodeViewset, base_name="code")
router.register(r'users', UserViewset, base_name="users")
router.register(r'userfavs', UserFavViewset, base_name="userfavs")
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")
# 配置订单的url
router.register(r'orders', OrderViewset, base_name="orders")

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api',include(router.urls)),
    url(r'docs/',include_docs_urls(title="天天生鲜")),
    url('api-token-auth/', views.obtain_auth_token),
    url('jwt-auth/', obtain_jwt_token),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
