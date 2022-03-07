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

