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

# 搭建项目环境
1. 在命令行处执行 python .\manage.py startapp login  创建一个app项目
2. 修改语言和时间，在 loginRegister 下面的seetings 中设置
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
#USE_TZ = True
USE_TZ = False  #是否使用时区

3. 运行项目
python .\manage.py runserver  8888 #指定端口
 也可以在  Run 里面点击编辑我的配置，设置端口和主机IP，然后点击运行即可运行项目


4.数据库
完成开启之后会发现后台打不开，/admin，此时需要对数据库进行操作

python .\manage.py makemigrations   #当数据库有改变时必须先执行此命令
python .\manage.py migrate          #迁移数据库,将生成的数据表写入数据库

python .\manage.py createsuperuser  #创建用户
用户名 (leave blank to use 'zxk'): admin
电子邮件地址: 123456@qq.com

# git提交代码到本地仓库
ssword:安装git,在 Terminal 中报错时，要设置他的环境变量。
1. 初始化git:  git init
Initialized empty Git repository in C:/Users/ZXK/PycharmProjects/day_08/loginRegister/.git/

2. 安装插件 .ignore ，并生成python上传文件需要忽略的内容

在File中的setting中设置 下载 ignore插件，安装之后，在新建时会有一个.ignore的扩展，
选择 .ignorefile  选择PYTHON之后便会有一个新文件。

3. 添加修改到暂存区
git add *   #将代码提交到暂存区
warning: in the working copy of '.idea/inspectionProfiles/Project_Default.xml', LF will be replaced by CRLF
the next time Git touches it
warning: in the working copy of '.idea/inspectionProfiles/profiles_settings.xml', LF will be replaced by CRL
F the next time Git touches it

4. 将暂存区的代码提交到本地git仓库
 git commit -m "创建项目环境" #提交代码到仓库

5. 查看历史提交记录
git log
Password (again):



#设计数据库模型
作为一个用户登录和注册项目，需要保存的都是各种用户的信息。很显然，我们至少需要一张用户表user,
在用户表里需要保存以下信息：
    用户名（name）：必填，最长不超过128个字符且唯一(unique)
    密码（password）：必填，最长不超过256个字符
    邮箱地址(email)：使用Django内置的邮箱类类型且唯一
    性别(gender)：性别，使用choice，只能选择男或者女，默认为男；
    创建时间(create_time):用户创建时间
        注意点：auto_now_add=True时为添加时的时间，更新对象不会有变动；
    修改时间(modify_time):用户最后一次修改时间
        注意点：auto_now=True时无论是添加还是修改对象，时间为你添加或者修改的时间
    最后一次登录时间(last_login_time):最后一次登录时间
        注意点：null=True 的话，数据库中该字段是NULL，即允许空值
        注意点：blank=False(默认)的话，字段没被赋值则会抛出异常，和数据验证(表单验证等)有关

1. login > models中创建数据库的类
# 设置数据库后端
Django 支持MYSQL、SQlite、oracle等数据库

# 注册APP　loginRegister／settings.py　
激活app到Django项目（注册app到Django项目)
在 INSTALLED_APPS 项目注册自己的项目 login

3. 生成迁移脚本并写入数据库
python manage.py makemigrations
python .\manage.py migrate


(loginRegister) PS C:\Users\ZXK\PycharmProjects\day_08\loginRegister> python .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, login, sessions
Running migrations:
  Applying login.0001_initial... OK

下载 ipython 会自动补全；
进入交互环境：python manage.py shell

# 测试
python.exe .\manage.py shell

插入数据：
from models import
In [1]: from login.models import SiteUser
In [2]: user1 = SiteUser(name="user1",passwoed="user1",email="user1@qq.com")
In [3]: user1.name
Out[3]: 'user1'

In [4]: user1.gender        #拿到一个默认值
Out[4]: 0
In [5]: user1.save()
In [6]: SiteUser.objects.all()
Out[6]: <QuerySet [<SiteUser: user1>]>
In [7]: user1.create_time
Out[7]: datetime.datetime(2023, 6, 3, 15, 37, 18, 52733, tzinfo=datetime.timezone.utc)

In [8]: user1.modify_time
Out[8]: datetime.datetime(2023, 6, 3, 15, 37, 18, 52733, tzinfo=datetime.timezone.utc)

In [9]: user1.last_login_time
In [12]: user1.passwoed = "newuser1"

In [13]: user1.passwoed
Out[13]: 'newuser1'

In [14]: user1.save()
In [15]: user1.create_time
Out[15]: datetime.datetime(2023, 6, 3, 15, 37, 18, 52733, tzinfo=datetime.timezone.utc)

In [16]: user1.last_login_time

In [17]: user1.modify_time
Out[17]: datetime.datetime(2023, 6, 3, 15, 40, 46, 814208, tzinfo=datetime.timezone.utc)

In [18]: user1.gender = 2
In [19]: user1.save()
In [20]: user1.modify_time
Out[20]: datetime.datetime(2023, 6, 3, 15, 42, 2, 100853, tzinfo=datetime.timezone.utc)

In [21]: user1.create_time
Out[21]: datetime.datetime(2023, 6, 3, 15, 37, 18, 52733, tzinfo=datetime.timezone.utc)
In [22]: user2 = SiteUser(name="user2",passwoed="user1",email="user1@qq.com")

In [23]: user2.email
Out[23]: 'user1@qq.com'
In [24]: user2.save()

IntegrityError: UNIQUE constraint failed: login_siteuser.email

(loginRegister) PS C:\Users\ZXK\PycharmProjects\day_08\loginRegister> git add *
(loginRegister) PS C:\Users\ZXK\PycharmProjects\day_08\loginRegister> git commit -m "添加数据库模型设置"
On branch master
nothing to commit, working tree clean
(loginRegister) PS C:\Users\ZXK\PycharmProjects\day_08\loginRegister> git log
commit bc771d2ae30da0b1235995d4df5c4892275273f7 (HEAD -> master)
Author: unknown <1002723982@qq.com>
Date:   Sun Jun 4 00:01:04 2023 +0800

    loginRegister 项目

# 数据库模型后台管理
loginRegister／admin.py　

from django.contrib import admin

from login.models import SiteUser

# Register your models here.
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ['name','gender','email']
    list_display_links = ['name']
    list_filter = ['gender','create_time']

# Alt + 回车自动导入
admin.site.register(SiteUser,SiteUserAdmin)
"""