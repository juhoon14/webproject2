from django.contrib import admin

from web.models import Cart, Item, Users, Category, ItemQna, MainQna, OrderDetail, Orderr, Review


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_number', 'u_id', 'p_number', 'product_count')
admin.site.register(Cart,CartAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_code', 'category_name')
admin.site.register(Category,CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'c_code', 'product_name', 'product_name', 'product_img', 'product_desc', 'product_desc_img', 'product_s_size', 'product_m_size', 'product_l_size', 'product_xl_size')
admin.site.register(Item,ItemAdmin)

class ItemQnaAdmin(admin.ModelAdmin):
    list_display = ('qna_number','p_number','u_id','u_pwd','qna_title','qna_desc','qna_date','qna_state');
admin.site.register(ItemQna,ItemQnaAdmin);

class MainQnaAdmin(admin.ModelAdmin):
    list_display = ('m_qna_number','u','u_pwd','m_qna_title','m_qna_desc','m_qna_date','m_qna_state');
admin.site.register(MainQna,MainQnaAdmin);

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order_detail_number','p_number','o_number','u','order_detail_name','order_detail_address','order_detail_phone');
admin.site.register(OrderDetail,OrderDetailAdmin);

class OrderrAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'u', 'order_date', 'order_status')
admin.site.register(Orderr,OrderrAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_number', 'p_number', 'u', 'review_img','review_desc')
admin.site.register(Review,ReviewAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_pwd','user_name','user_phone','user_email','user_address1','user_address2','user_auth');
admin.site.register(Users,UserAdmin);



