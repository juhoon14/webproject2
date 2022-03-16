from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
# Create your views here.
# coding:utf-8
from web.models import Users, Item


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def index(self,request):
        objs = Item.objects.all();
        print(objs.query);
        context = {
            'center': 'item/list.html',
            'objs': objs
        };
        return render(request,'index.html', context)

    @request_mapping("/cart", method="get")
    def cart(self, request):

        context = {
            'center': 'cart.html',
        };

        return render(request, 'home.html', context);



    @request_mapping("/popular", method="get")
    def popular(self, request):
        objs = Item.objects.all();
        context = {
            'center': 'popular.html',
            'objs':objs
        };
        return render(request, 'home.html', context);

    @request_mapping("/new", method="get")
    def new(self, request):
        objs = Item.objects.all();
        context = {
            'center': 'new.html',
            'objs':objs
        };
        return render(request, 'home.html', context);




    # @request_mapping("register", method="get")
    # def register(self, request):
    #
    #     return render(request, 'register.html')
    #
    # @request_mapping("registerimpl", method="post")
    # def registerimpl(self, request):
    #     id = request.POST['id']
    #     pwd = request.POST['pwd']
    #     name = request.POST['name']
    #     addr = request.POST['addressName1']+' '
    #     addr += request.POST['addressName2']
    #     phone = request.POST['phone']
    #     phone += request.POST['mid']
    #     phone += request.POST['last']
    #     email = request.POST['emailId']+'@'
    #     email += request.POST['emailaddress']
    #     context = {}
    #     try:
    #         Users(user_id=id, user_pwd=pwd, user_name=name, user_phone=phone,
    #               user_email=email, user_address=addr).save()
    #         context['center'] = 'registerok.html'
    #         context['id'] = id
    #     except:
    #         context['center'] = 'registerfail.html'
    #
    #     return render(request, 'index.html', context)
    #
    # @request_mapping("/registerimplid", method="get")
    # def registerimplid(self, request):
    #     id = request.GET.get('input_id')
    #     context = {}
    #     try:
    #         Users.objects.get(user_id=id)
    #         context['data'] = '사용할 수 없는 ID 입니다..'
    #     except:
    #         context['data'] = '사용할 수 있는 ID 입니다.'
    #
    #     return JsonResponse(context)
    #
    # @request_mapping("/registerimplpwd", method="get")
    # def registerimplpwd(self, request):
    #     pwd1 = request.GET.get('input_pw1')
    #     pwd2 = request.GET.get('input_pw2')
    #     context = {}
    #     try:
    #         if pwd1 == pwd2:
    #             context['data'] = '비밀번호가 일치합니다.'
    #         else:
    #             Exception
    #     except:
    #         context['data'] = '비밀번호가 일치하지 않습니다.'
    #
    #     return JsonResponse(context)
    #
    # @request_mapping("/login", method="get")
    # def login(self, request):
    #     return render(request, 'login.html')
    #
    # @request_mapping("loginimpl", method="post")
    # def loginimpl(self, request):
    #     objs = Item.objects.all();
    #     id = request.POST['id']
    #     pwd = request.POST['pwd']
    #
    #     try:
    #         Users.objects.get(user_id=id, user_pwd=pwd)
    #         request.session['sessionid'] = id
    #         context = {
    #             'center': 'item/list.html',
    #             'objs': objs
    #         };
    #         return render(request, 'index.html', context)
    #     except:
    #         context['center'] = 'login.html'
    #         context['print'] = "아이디 혹은 비밀번호를 다시 입력해주세요."
    #         return render(request, context['center'], context)
    #
    # @request_mapping("logout", method="get")
    # def logout(self, request):
    #     objs = Item.objects.all();
    #     if request.session['sessionid'] != None:
    #         del request.session['sessionid']
    #     context = {
    #         'center': 'item/list.html',
    #         'objs': objs
    #     };
    #     return render(request, 'index.html', context)
