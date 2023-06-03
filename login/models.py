from django.db import models

# Create your models here.

# 默认数据库表名 appname_siteuser
class SiteUser(models.Model):
    """用户的数据库模型。注册/登录需要"""
    #元组里面嵌套元组
    gendev_choice = (
        (0, "未知"),
        (1, "男"),
        (2, "女"),
    )
    # 字符串 CharField 必须指定最大长度
    name = models.CharField(max_length=128,unique=True,verbose_name="用户名")
    passwoed = models.CharField(max_length=256,verbose_name="密码")
    email = models.EmailField(unique=True,verbose_name="电子邮箱")
    gender = models.IntegerField(choices=gendev_choice,default=0,verbose_name="性别")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modify_time = models.DateTimeField(auto_now=True,verbose_name="最后一次修改时间")
    # null 是针对数据库层面的，insert,  blank 针对表单
    last_login_time = models.DateTimeField(null=True,blank=True,verbose_name="最后一次登录的时间")

    #定义默认输出格式，中文友好展示
    def __str__(self):
        return self.name

    class Meta:
        #db_table = "books"  #自定义表名
        verbose_name = "网站用户管理"         #单数时显示的名称
        verbose_name_plural = verbose_name  #复数时显示的名称

