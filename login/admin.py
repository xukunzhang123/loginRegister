from django.contrib import admin

from login.models import SiteUser

# Register your models here.

# 后台管理设置的信息
class SiteUserAdmin(admin.ModelAdmin):
    list_display =  ['name', 'gender', 'email']
    list_display_links =  ['name']
    list_filter = ['gender','create_time']


# Alt + 回车自动导入
admin.site.register(SiteUser,SiteUserAdmin)