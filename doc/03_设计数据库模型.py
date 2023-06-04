"""
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
"""