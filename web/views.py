from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
# Create your views here.



@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def index(self,request):
        return render(request,'index.html');

    @request_mapping("/cart", method="get")
    def cart(self, request):

        context = {
            'center': 'cart.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/top", method="get")
    def top(self, request):

        context = {
            'center': 'top/top.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/bottom", method="get")
    def bottom(self, request):

        context = {
            'center': 'bottom/bottom.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/popular", method="get")
    def popular(self, request):

        context = {
            'center': 'popular.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/new", method="get")
    def new(self, request):

        context = {
            'center': 'new.html',
        };
        return render(request, 'home.html', context);