"""
 shift +Tab 快速取消缩进
 CTRL + /   快速注释

python中已经自带了session插件，在loginRegister/settings.py 中的INSTALLED_APPS 'django.contrib.sessions',
登录成功，存储登录的用户信息到session中
login/views.py

if user:
    # 用户存在
    request.session['is_login'] = True
    request.session['user_id'] = user.id
    request.session['username'] = user.name
    return redirect('/index/')

当用户登出的时候清除session信息

def logout(request):
    #如果状态不是登录状态无法登出
    if request.session.get('is_login'):
        request.session.flush() #清空session信息
    # redirect 重定向，跳转
    return redirect('/login/')

在首页添加登出超链接并测试：
templates/login/index.html

<h1> 你好啊！{{ request.session.username }} ,  这是首页的模板界面!! </h1>
<a href="/logout/"><strong style="font-size: medium">登出</strong></a>

"""