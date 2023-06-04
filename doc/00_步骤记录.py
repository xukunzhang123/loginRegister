"""
# 项目开始前的思考
1. 路由配置
urlpatterns = [
    path('/register/', views.register),
    path('/login/', views.login),
    path('/logout/', views.logout),
]
2.试图配置（重点）

3.数据库模型 Model

class User:
        id ，name,password,email,create_time,update_time,
        last_time（最后一次登录时间）,gender,provice
4.模板 Template: register.html ,login.html , logout.html

#设计数据库模型

# 数据库模型后台管理

#路由试图函数框架搭建

#前端界面设计与优化
"""

