from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
# Create your views here.



@request_mapping("/top")
class TopView(View):

################상의
    @request_mapping("/1", method="get")
    def top1(self, request):

        context = {
            'center': 'top/top1.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/2", method="get")
    def top2(self, request):

        context = {
            'center': 'top/top2.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/3", method="get")
    def top3(self, request):

        context = {
            'center': 'top/top3.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/4", method="get")
    def top4(self, request):

        context = {
            'center': 'top/top4.html',
        };
        return render(request, 'home.html', context);
