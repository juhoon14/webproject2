from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
# Create your views here.



@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def index(self,request):
        return render(request,'index.html')

    @request_mapping("/a", method="get")
    def all(self, request):

        context = {
            'center': 'view_option.html',
        }
        return render(request, 'home.html', context);

    @request_mapping("/top", method="get")
    def top(self, request):

        context = {
            'center': 'top.html',
        }
        return render(request, 'home.html', context);

    @request_mapping("/bottom", method="get")
    def bottom(self, request):

        context = {
            'center': 'bottom.html',
        }
        return render(request, 'home.html', context);
