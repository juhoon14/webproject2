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
<<<<<<< HEAD
        return render(request, 'index.html', context);
=======
        return render(request, 'home.html', context);
>>>>>>> cd94c2b42611941e8889eecbd6a1e964cdbc2efc

    @request_mapping("/top", method="get")
    def top(self, request):

        context = {
            'center': 'top.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/bottom", method="get")
    def bottom(self, request):

        context = {
            'center': 'bottom.html',
        };
        return render(request, 'home.html', context);
