"""
数据库模型后台管理
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

[04/Jun/2023 00:18:54] "GET /admin/jsi18n/ HTTP/1.1" 200 8560
"""