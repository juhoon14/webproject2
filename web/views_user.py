from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping
from django.http import JsonResponse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import string
import random
# Create your views here.

from web.models import Users


def email_auth_num():
    LENGTH = 8
    string_pool = string.ascii_letters + string.digits
    auth_num = ""
    for i in range(LENGTH):
        auth_num += random.choice(string_pool)
    return auth_num


@request_mapping("/user")
class UserView(View):

    @request_mapping("/register", method="get")
    def register(self, request):
        return render(request, 'user/register.html')

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        context = {}
        id = request.POST['id']
        pwd = request.POST['pwd']
        name = request.POST['name']
        addr = request.POST['addressName1'] + ' '
        addr += request.POST['addressName2']
        phone = request.POST['phone']
        email = request.POST['email']
        try:
            Users.objects.get(user_id=id)
            context['error'] = "이미 존재하는 아이디 입니다."
            return render(request, "user/register.html", context)
        except:
            Users(user_id=id, user_pwd=pwd, user_name=name, user_phone=phone,
                  user_email=email, user_address=addr).save()
            return redirect("/user/login")

    @request_mapping("/registerimplid", method="get")
    def registerimplid(self, request):
        id = request.GET.get('input_id')
        context = {}
        try:
            Users.objects.get(user_id=id)
            context['data'] = 1
        except:
            context['data'] = 0
        return JsonResponse(context)

    @request_mapping("/registerimplpwd", method="get")
    def registerimplpwd(self, request):
        pwd1 = request.GET.get('input_pw1')
        pwd2 = request.GET.get('input_pw2')
        context = {}
        try:
            if pwd1 == pwd2:
                context['data'] = '비밀번호가 일치합니다.'
            else:
                Exception
        except:
            context['data'] = '비밀번호가 일치하지 않습니다.'

        return JsonResponse(context)

    @request_mapping("/login", method="get")
    def login(self, request):
        return render(request, 'user/login.html')

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        id = request.POST['id']
        pwd = request.POST['pwd']
        context = {}
        try:
            user = Users.objects.get(user_id=id, user_pwd=pwd)
            request.session['sessionid'] = user.user_id
            request.session['sessionname'] = user.user_name
            return redirect("/")
        except:
            context['center'] = 'user/login.html'
            context['print'] = "아이디 혹은 비밀번호를 다시 입력해주세요."

        return render(request, context['center'], context)

    @request_mapping("/logout", method="get")
    def logout(self, request):
        if request.session['sessionid'] != None:
            del request.session['sessionid']
        return redirect("/")

    @request_mapping("/idserchimpl", method="post")
    def idserchimpl(self, request):
        name = request.POST['name']
        phone = request.POST['phone']
        try:
            obj = Users.objects.get(user_name=name, user_phone=phone)
            context = {'id': obj.user_id}
            return render(request, "user/idserch_ch.html", context)
        except:
            context = {'print': '일치하는 이름 또는 핸드폰번호가 없습니다.'}
        return render(request, "user/idserch.html", context)

    @request_mapping("/idserch", method="get")
    def idserch(self, request):
        return render(request, 'user/idserch.html')

    @request_mapping("/pwdserch", method="get")
    def pwdserch(self, request):
        return render(request, 'user/pwdserch.html')

    @request_mapping("/pwdserchimpl", method="get")
    def pwdserchimpl(self, request):
        id = request.GET.get('input_id')
        name = request.GET.get('input_name')
        email = request.GET.get('input_email')
        try:
            obj = Users.objects.get(user_id=id, user_name=name, user_email=email)
            message = email_auth_num()

            obj.user_auth = message
            obj.save()

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("aossuper12", "wjdals312!")

            mail_html = "<html><body><h1>"+message+" 코드를 입력해주세요"+"</h1></body></html>"

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "머&이 비밀번호 찾기 메일 입니다."
            msg['From'] = "aossuper12@gmail.com"
            msg['To'] = email
            mail_html = MIMEText(mail_html, 'html')
            msg.attach(mail_html)

            server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
            server.quit()

            return JsonResponse()
        except:
            context = {'print':"해당하는 정보가 없습니다."}
        return render(request, "user/pwdserch.html", context)

    @request_mapping("/pwdserchimpl2", method="get")
    def pwdserchimpl2(self, request):
        emailch = request.GET.get('email_ch')
        id = request.GET.get('input_id')
        context = {}
        try:
            obj = Users.objects.get(user_id=id)
            if emailch == obj.user_auth:
                context['data'] = 1
                return JsonResponse(context)
            else:
                raise Exception
        except:
            context['data'] = 0
            return JsonResponse(context)

    @request_mapping("/pwdserchsave", method="post")
    def pwdserchsave(self, request):
        id = request.POST['id']
        pwd = request.POST['pwd']
        try:
            obj = Users.objects.get(user_id=id)
            obj.user_pwd = pwd
            obj.save()
            return redirect("/user/login")
        except:
            context = {'print':'비밀번호 바꾸기 오류 관리자에게 문의하세요'}
        return render(request, "/user/pwdserch.html", context)