from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
# Create your views here.



@request_mapping("/bottom")
class BottomView(View):

#############하의############

    @request_mapping("/5", method="get")
    def bottom5(self, request):

        context = {
            'center': 'bottom/bottom5.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/6", method="get")
    def bottom6(self, request):

        context = {
            'center': 'bottom/bottom6.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/7", method="get")
    def bottom7(self, request):

        context = {
            'center': 'bottom/bottom7.html',
        };
        return render(request, 'home.html', context);

    @request_mapping("/8", method="get")
    def bottom8(self, request):

        context = {
            'center': 'bottom/bottom8.html',
        };
        return render(request, 'home.html', context);
