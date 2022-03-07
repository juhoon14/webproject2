from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping
# Create your views here.

from web.models import Users


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def index(self,request):
        return render(request,'index.html');

    @request_mapping("/a", method="get")
    def all(self, request):

        context = {
            'center': 'view_option.html',
        };
        return render(request, 'index.html', context);

    @request_mapping("register", method="get")
    def register(self, request):
        context={'center':'register.html'}
        return render(request, 'index.html', context)

    @request_mapping("registerimpl", method="post")
    def registerimpl(self, request):
        id = request.POST['id']
        pwd = request.POST['pwd']
        name = request.POST['name']
        addr = request.POST['addressName1']+' '
        addr += request.POST['addressName2']
        phone = request.POST['phone']
        phone += request.POST['mid']
        phone += request.POST['last']
        email = request.POST['emailId']+'@'
        email += request.POST['emailaddress']
        context = {}
        try:
            Users(user_id=id, user_pwd=pwd, user_name=name, user_phone=phone,
                  user_email=email, user_address=addr).save()
            context['center'] = 'registerok.html'
            context['id'] = id
        except:
            context['center'] = 'registerfail.html'

        return render(request, 'index.html', context)

    @request_mapping("/registerimplid", method="get")
    def registerimplid(self, request):
        id = request.GET.get('input_id')
        context = {}
        try:
            Users.objects.get(user_id=id)
            context['data'] = '사용할 수 없는 ID 입니다.'
        except:
            context['data'] = '사용할 수 있는 ID 입니다.'

        return JsonResponse(context)

    @request_mapping("/login", method="get")
    def login(self, request):
        context = {'center':'login.html'}
        return render(request, 'index.html', context)

    @request_mapping("loginimpl", method="post")
    def loginimpl(self, request):
        id = request.POST['id']
        pwd = request.POST['pwd']
        context = {}
        try:
            Users.objects.get(user_id=id, user_pwd=pwd)
            request.session['sessionid'] = id
            context['center'] = 'loginok.html'
        except:
            context['center'] = 'login.html'
            context['print'] = "아이디와 비밀번호를 다시 입력해주세요."

        return render(request, 'index.html', context)

    @request_mapping("logout", method="get")
    def logout(self, request):
        if request.session['sessionid'] != None:
            del request.session['sessionid']
        return render(request, 'index.html')