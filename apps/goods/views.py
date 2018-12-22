from django.shortcuts import render
# Create your views here.
# from .serializers import GoodsSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response

from .serializer import GoodsSerializer,CategorySerializer
from rest_framework import mixins, generics, status,viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Goods,GoodsCategory
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend


# 商品分页
class GoodsPagination(PageNumberPagination):
    page_size =10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# 商品列表页继承API视图
# viewsets实现商品列表页 GenericView完成商品列表和分页
class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    # 序列化
    serializer_class = GoodsSerializer
    # 分页
    paignation_class = GoodsPagination
    # 过滤器
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    # 搜索 排序
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer