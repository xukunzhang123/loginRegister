import hashlib
import  datetime

from django.core.mail import send_mail

from login.models import ConfirmString
from loginRegister import settings


def hash_code(s, salt='mysite'): #加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  #update方法只接收bytes类型
    return h.hexdigest()

def make_confirm_string(user):
    print("生成确认码....")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    print('in code:',code)
    ConfirmString.objects.create(code=code, user=user)
    return code

def send_email(email, code):
    print('send mail ......')
    subject = '注册确认邮箱'
    text_content = '''感谢注册，这里是登录系统注册网站！\
                    如果你看到这个消息，说明您的邮箱服务器不提供HTML链接功能，请联系管理员！'''
    html_content = '''
    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>点击认证</a>,\
    这里是登录注册系统网站！</p>
    <p>请点击站点链接完成注册确认</p>
    <p>此链接有效期为{}天！</p>
    '''.format('127.0.0.1:8888', code, settings.CONFIRM_DAYS)

    send_mail(subject, text_content, settings.EMAIL_HOST_USER, [email,],
              html_message = html_content )
