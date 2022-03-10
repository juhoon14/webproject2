from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
# Create your views here.

from web.models import Users


@request_mapping("/item")
class itemView(View):

    @request_mapping("/i", method="get")
    def insert(self,request):
        context = {'center':'/item/itemadd.html'}
        return render(request,'index.html', context);