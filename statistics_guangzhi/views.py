from django.core import serializers
from django.http import JsonResponse, HttpResponse

# Create your views here.
import json

from django.views.decorators.http import require_http_methods
from requests import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenViewBase

from statistics_guangzhi.models import Student
from statistics_guangzhi.serializers import MyTokenSerializer

"""
登录
"""


class Login(TokenViewBase):
    serializer_class = MyTokenSerializer

    # post方法对应post请求，登陆时post请求在这里处理
    def post(self, request, *args, **kwargs):
        # 使用刚刚编写时序列化处理登陆验证及数据响应
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise ValueError(f'验证失败： {e}')

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


# 用于演示后台获取token中payload数据的视图
class DemoView(APIView):

    def get(self, request):
        # 通过request.auth获取用户Token
        print('请求用户Token为：')
        print(request.auth)

        # 通过request.auth.payload可以获取到解析后的payload内容（字典类型）
        print("\n有效荷载信息：")
        print(request.auth.payload)

        return HttpResponse('身份验证通过！', status=status.HTTP_200_OK)


"""
学生信息
"""


@require_http_methods(["GET"])
def add_student(request):
    response = {}
    try:
        student = Student(student_name=request.GET.get('student_name'), student_id=request.GET.get('student_id'))
        student.save()
        response['msg'] = "success"
        response['error_num'] = 0
    except Exception as e:
        print(e)

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_students(request):
    response = {}

    try:

        students = Student.objects.filter()

        response['list'] = json.loads(serializers.serialize("json", students))

        response['msg'] = 'success'

        response['error_num'] = 0

    except Exception as e:

        response['msg'] = str(e)

        response['error_num'] = 1

    # return JsonResponse(response, content_type='application/json,charset=utf-8')
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


"""
同步相关
"""


def sync_grades_students(request):
    response = {}

    try:

        print(123)

    except Exception as e:

        response['msg'] = str(e)

        response['error_num'] = 1

        # return JsonResponse(response, content_type='application/json,charset=utf-8')
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')
