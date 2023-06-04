"""
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

"""