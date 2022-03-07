from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
# Create your views here.



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

        context = {'center': 'registerok.html', 'id':id, 'pwd':pwd,'name':name,
                   'addr':addr, 'phone':phone, 'email':email}
        return render(request, 'index.html', context)