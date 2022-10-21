"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from statistics_guangzhi import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from statistics_guangzhi.views import Login, DemoView

urlpatterns = [
    path('login/', Login.as_view()),
    path('loginTest/', DemoView.as_view()),
    path('admin/', admin.site.urls),
    path('add_student/', views.add_student),
    path('show_students/', views.show_students),
    # token获取路由，访问这个路由可以获取token信息包含access和refresh，请求方式为post，需要携带username与password 这两个是固定参数
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新token,请求方式post需要携带refresh，返回数据会获得一个信息的access
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 认证token,post请求，json形式传参{"token":access} token为固定参数名称
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
