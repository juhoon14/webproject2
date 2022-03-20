from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping
from django.db.models import Count
# Create your views here.

from web.models import Users, Cart, Orderr, Item


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def index(self, request):
        objs = Item.objects.all();
        context = {
            'center': 'item/list.html',
            'objs': objs
        };
        return render(request, 'index.html', context)

    @request_mapping("/popular", method="get")
    def popular(self, request):
        objs = Item.objects.all();
        context = {
            'center': 'popular.html',
            'objs': objs
        };
        return render(request, 'home.html', context);

    @request_mapping("/new", method="get")
    def new(self, request):
        objs = Item.objects.all();
        context = {
            'center': 'new.html',
            'objs': objs
        };
        return render(request, 'home.html', context);

    @request_mapping("/a", method="get")
    def all(self, request):
        context = {'center': 'view_option.html'}
        return render(request, 'home.html', context)

    @request_mapping("/cart", method="get")
    def cart(self, request):
        obj = Cart.objects.filter(u_id=request.session['sessionid']).select_related('u','p_number')
        print(obj.query)
        context = {'center':'cart.html', 'obj':obj}
        return render(request, 'index.html', context)

    @request_mapping("/cartdelete", method="get")
    def cartdelete(self, request):
        num = request.get('num')
        Cart.objects.get(cart_number=num).delete()
        return redirect("/cart")

    @request_mapping("/cartmodify", method="get")
    def cartmodify(self, request):
        num = request.GET.get('input_num')
        qua = request.GET.get('input_quantity')
        obj = Cart.objects.get(cart_number=num)
        obj.product_count = qua
        obj.save()
        return JsonResponse({'data':1})

    @request_mapping("/order", method="get")
    def order(self, request):
        obj = Cart.objects.all()
        user = Users.objects.get(user_id=request.session['sessionid'])
        context = {'center':'order.html', 'obj':obj, 'user':user}
        return render(request, 'index.html', context)

    @request_mapping("/ordercomplete", method="get")
    def ordercomplete(self, request):
        name = request.GET.get('name')
        addr1 = request.GET.get('addr1')
        addr2 = request.GET.get('addr2')
        phone = request.GET.get('phone')
        msg = request.GET.get('msg')
        obj = Cart.objects.get(u_id=request.session['sessionid'])
        Orderr(u_id=request.session['sessionid'], order_name=name,
               order_phone=phone, order_addr1=addr1, order_addr2=addr2, order_msg=msg,
               order_status='결제완료').save()
        ord = Orderr.objects.get(u_id=request.session['sessionid'])
        ord.p_number = obj.p_number
        ord.save()

        return JsonResponse({'data':1})

    @request_mapping("/ordercomplate2", method="get")
    def ordercomplate2(self, request):
        context = {'center': 'ordercomplate.html'}
        return render(request, 'index.html', context)