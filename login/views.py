from django.shortcuts import render, redirect

from login.models import SiteUser


# Create your views here.

def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    # print(request.method) #加上{% csrf_token %} 请求从GET 变为 POST
    if request.method == "POST":
        # print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': ['xUyK3Ml4vad1hK2amnUK9q7zfkqMmsUH7MzfM1CZdf6342EYzx2dllv1OPQVZaBc']}>
        # 在前端加上name之后便可得到信息
        # <QueryDict: {'csrfmiddlewaretoken': ['ELHyNfYu44549l6Oh1BEzae9sUD8y6rXeDI3wufpM9Y6WDICubJ7L5CB1p3hbO8s'], 'username': ['user1'], 'password': ['user1']}>
        # 拿到登录信息之后便能可以去数据库对比
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        if username and password:
            # 1.用户名是否合法（在数据库中是否存在）
            # 密码是否合法（填写的密码是否和数据库一致）
            # 其他验证
            user = SiteUser.objects.filter(name=username, passwoed=password).first()
            if user:
                # 用户存在
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['username'] = user.name
                return redirect('/index/')
            else:
                message = "用户名或密码错误"
                return render(request, 'login/login.html',{'message':message})
        else:
            message = "非法的数据信息"
            return render(request, 'login/login.html', {'message': message})
        #return redirect('/index/')
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    #如果状态不是登录状态无法登出
    if request.session.get('is_login'):
        request.session.flush() #清空session信息
    # redirect 重定向，跳转
    return redirect('/login/')
