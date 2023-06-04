"""
# 路由试图函数框架搭建
1. 路由设计
URL           视图views                   模板               功能
/index/       login.views.index           index.html        首页
/login/       login.views.login           loogin.html       登录页面
/register/    login.views.register        register.html     注册页面
/logout/      login.views.logout          无须返回页面        登出界面

访问策略：
    未登录人员，不论是访问index还是logout和login ,全部跳转到login页面
    已登录人员，访问login会自动跳转到index页面
    已登录人员，不允许直接访问register页面，需要先logout
    登出后，自动跳转到login页面

1. 主路由配置文件
# loginRegister/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),    #添加的行，如果没有前缀，访问子路由配置文件
]

2. 子路由配置文件（login子应用的）
# login/urls.py （新建的文件）

from django.urls import path, include
from login import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('logout/', views.logout,name='logout'),
]

3. 视图函数配置
# login/views.py

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    pass
    return render(request,'login/login.html')

def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    pass
    #redirect 重定向，跳转
    return redirect('/login/')

4. 模板template的配置
#templates/login/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
<h1>这是首页的模板界面</h1>
</body>
</html>

#templates/login/login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户登录</title>
</head>
<body>
<h1>用户登录</h1>
<form>
    用户名：<input type="text" placeholder="username"><br/>
    密码：<input type="password" placeholder="password"><br/>
    <input type="submit" placeholder="登录">
</form>
</body>
</html>

#templates/login/register.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户注册</title>
</head>
<body>
<h1>用户注册页面</h1>
<form>
    用户名：<input type="text" placeholder="username"><br/>
    电子邮箱：<input type="email" placeholder="email"><br/>
    密码：<input type="password" placeholder="password"><br/>
    确认密码：<input type="password" placeholder="password"><br/>
    <input type="submit" placeholder="注册">
</form>
</body>
</html>

5. 测试 （浏览器访问）
http://127.0.0.1:8888/register/
http://127.0.0.1:8888/login/
http://127.0.0.1:8888/index/
"""