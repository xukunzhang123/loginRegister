from datetime import datetime, timedelta

from django.shortcuts import render, redirect

from login.forms import LoginForm, RegisterForm
from login.models import SiteUser, ConfirmString
from login.utils import hash_code, make_confirm_string, send_email
from loginRegister import settings


# Create your views here.


def index(request):
    return render(request, 'login/index.html')


def login(request):
    # print(request.method) #加上{% csrf_token %} 请求从GET 变为 POST
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            # print(request.POST)
            # <QueryDict: {'csrfmiddlewaretoken': ['xUyK3Ml4vad1hK2amnUK9q7zfkqMmsUH7MzfM1CZdf6342EYzx2dllv1OPQVZaBc']}>
            # 在前端加上name之后便可得到信息
            # <QueryDict: {'csrfmiddlewaretoken': ['ELHyNfYu44549l6Oh1BEzae9sUD8y6rXeDI3wufpM9Y6WDICubJ7L5CB1p3hbO8s'], 'username': ['user1'], 'password': ['user1']}>
            # 拿到登录信息之后便能可以去数据库对比
            # username = request.POST.get('username').strip()
            # password = request.POST.get('password').strip()
            # if username and password:
            # 1.用户名是否合法（在数据库中是否存在）
            # 密码是否合法（填写的密码是否和数据库一致）
            # 其他验证
            user = SiteUser.objects.filter(name=username, passwoed=hash_code(password)).first()
            if user:
                if not user.has_confirmed:
                    message = "该用户未进行邮件确认!"
                    return render(request, 'login/login.html', locals())
                # 用户存在is_login
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['username'] = user.name
                return redirect('/index/')
            else:
                message = "用户名或密码错误"
                # return render(request, 'login/login.html',{'message':message})
                return render(request, 'login/login.html', locals())
        else:
            message = "填写的登录信息不合法"
            # return render(request, 'login/login.html', {'message': message})
            return render(request, 'login/login.html', locals())
        # return redirect('/index/')
    login_form = LoginForm()
    return render(request, 'login/login.html', locals())


def register(request):
    # 如果用户已经登录，则不能注册跳转到首页
    if request.session.get('is_login', None):
        return redirect('/index/')

    # 如果是POST请求，先验证提交的数据是否通过，
    if request.method == 'POST':
        print(request.POST)
        register_form = RegisterForm(request.POST)
        message = "请检查你填写的内容！"
        # print(message)
        # 清洗数据
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            # 接下来判断用户名和邮箱是否已经被注册，跳转到登录页面
            print(locals())
            same_name_user = SiteUser.objects.filter(name=username)
            if same_name_user:
                message = "用户名已经存在！"
                return render(request, 'login/register.html', locals())
            same_email_user = SiteUser.objects.filter(email=email)
            print(same_email_user)
            if same_email_user:
                message = "该邮箱已经被注册了！"
                return render(request, 'login/register.html', locals())
            try:    #抛出异常
                # 将注册的数据存储到数据库，跳转到登录页面
                new_suer = SiteUser(name=username, passwoed=hash_code(password1), email=email)
                new_suer.save()
                # 生成邮件确认码并发送邮件确认
                code = make_confirm_string(new_suer)
                send_email(email, code)
                message = '请前往邮箱进行确认!'
            except  Exception:
                new_suer.delete()
                message = "发送邮件失败！"
                return render(request, 'login/register.html', locals())
            else:
                return redirect('/login/')
    # 如果是GET请求，返回用户注册的html页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    # 如果状态不是登录状态无法登出
    if request.session.get('is_login'):
        request.session.flush()  # 清空session信息
    # redirect 重定向，跳转
    return redirect('/login/')

def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求'
        return render(request, 'login/confirm.html', locals())

    create_time = confirm.create_time
    now = datetime.now()
    if now > create_time + timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册！'
    else:
        confirm.user.is_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = "感谢确认，请使用账户登录！"
    return render(request, 'login/confirm.html', locals())

