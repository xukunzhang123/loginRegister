"""
html 和视图函数交互的完善

# templates/login/login.html
<div class="col-sm">
    <h3 style="text-align: center">用户登录</h3>
    <!-- 告警 <strong>登录失败!</strong> 加粗；
        alert-primary 浅蓝色
        alert-danger  红色
        alert-warning 浅黄色
        -->
1. 有message信息则显，没有就不显示
    {% if message %}
    <div class="alert alert-warning" role="alert">
        <strong>登录失败!</strong> {{ message }}
    </div>
    {% endif %}
2.提交登录信息时，以post方法提交给/login/对应的视图函数处理。
    <!-- form action="/login/" method="post"
        当用户点击登录时，以post方法执行/login/路由对应的视图函数
        没加上之前默认是GET 请求
        加上之后点击登录会提示csrf报错，需要加上 {% csrf_token %}
        加上之后此时再次登陆会变为POST请求
        。-->
    <form action="/login/" method="post">
3.Django提供了csrf防攻击的机制，添加该信息则可顺利访问登录页面
        {% csrf_token %}
        <div class="form-group">
            <label>用户名</label>
4. name="username" 指定表单内容存储的key名称，eg:{“username”:“你填写的用户名"}
            <input type="text" class="form-control" name="username">
        </div>
        <div class="form-group">
            <label>密码</label>
5. name="username" 指定表单内容存储的key名称，eg:{“username”:“你填写的用户名"}
            <input type="password" class="form-control" name="password">
            <small class="form-text text-muted">密码必须是字母、数字和特殊符号组成.</small>
        </div>
        <!-- float-right 将按钮飘到右侧 -->
        <!-- a 标签是添加链接，<ins>新用户注册</ins> 为标签添加下划线 class="text-success" 控制颜色success绿色，error红色-->
        <a href="/register/" class="text-success">
            <ins>新用户注册</ins>
        </a>
        <button type="submit" class="btn btn-primary float-right">登录</button>
    </form>
</div>

 视图函数的完善
login/views.py
from login.models import SiteUser

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
            user = SiteUser.objects.filter(name=username,passwoed=password).first()
            if user:
                # 用户存在
                return redirect('/index/')
            else:
                message = "用户名或密码错误"
                return render(request, 'login/login.html',{'message':message})
        else:
            message = "非法的数据信息"
            return render(request, 'login/login.html', {'message': message})
        #return redirect('/index/')
    return render(request, 'login/login.html')

3. 测试是否成功
http://127.0.0.1:8888/login/
"""
