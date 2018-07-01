from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from .serializer import SmsSerializer,UserRegSerializer
from rest_framework.response import Response
from rest_framework import status
from utils.yunpian import YunPian
from super.settings import APIKEY
from random import choice
from .models import VerifyCode
from django.core import serializers

User = get_user_model()

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            #用户名和手机都能登录
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# class SmsCodeViewset(CreateModelMixin,viewsets.GenericViewSet):
#     '''
#     手机验证码
#     '''
#     serializer_class = SmsSerializer
#
#     def generate_code(self):
#         """
#         生成四位数字的验证码
#         """
#         seeds = "1234567890"
#         random_str = []
#         for i in range(4):
#             random_str.append(choice(seeds))
#
#         return "".join(random_str)
#
#         # 输入密码的时候不显示明文
#
#
#
#
#
#
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         #验证合法
#         serializer.is_valid(raise_exception=True)
#
#         mobile = serializer.validated_data["mobile"]
#
#         yun_pian = YunPian(APIKEY)
#         #生成验证码
#         code = self.generate_code()
#
#         sms_status = yun_pian.send_sms(code=code, mobile=mobile)
#
#         if sms_status["code"] != 0:
#             return Response({
#                 "mobile": sms_status["msg"]
#             }, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             code_record = VerifyCode(code=code, mobile=mobile)
#             code_record.save()
#             return Response({
#                 "mobile": mobile
#             }, status=status.HTTP_201_CREATED)

class UserViewset(CreateModelMixin,viewsets.GenericViewSet):
    '''
    用户
    '''
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()