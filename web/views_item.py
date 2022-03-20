import logging

from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from config.settings import UPLOAD_DIR
from web.models import Item, Category


@request_mapping("/item")
class ItemView(View):

    @request_mapping("/a", method="get")
    def all(self,request):
        objs = Item.objects.all();
        context = {
            'center':'item/list.html',
            'objs':objs
        };
        return render(request,'home.html', context);

    @request_mapping("/top", method="get")
    def top(self, request):
        objs = Item.objects.all();
        context = {
            'center': 'top/top.html',
            'objs': objs
        };
        return render(request, 'home.html', context);

    @request_mapping("/bottom", method="get")
    def bottom(self, request):
        objs = Item.objects.all();
        context = {
            'center': 'bottom/bottom.html',
            'objs': objs
        };
        return render(request, 'home.html', context);

    @request_mapping("/iv", method="get")
    def insertview(self,request):
        catg = Category.objects.all();
        # print(catg.query);
        context = {
            'center':'item/itemadd.html',
            'catg':catg
        };
        return render(request,'home.html',context);

    @request_mapping("/ii", method="post")
    def insert(self,request):
        name = request.POST['product_name'];
        price = request.POST['product_price'];
        desc = request.POST['product_desc'];
        catg = request.POST['c_code'];
        imgname = '';
        if 'product_img' in request.FILES:
            img = request.FILES['product_img'];
            imgname = img._name;
            f = open('%s/%s' % (UPLOAD_DIR, imgname), 'wb')
            for chunk in img.chunks():
                f.write(chunk);
                f.close();

        cate = Category.objects.get(category_code=catg);
        obj = Item(product_name=name, product_price=price, product_img=imgname, product_desc=desc, c_code=cate);
        obj.save();

        return redirect('/item/a');

    @request_mapping("/g/<int:pk>/", method="get")
    def get(self,request,pk):
        obj = Item.objects.get(product_number=pk);

        context = {
            'center':'item/get.html',
            'obj':obj
        };
        return render(request,'home.html',context);

