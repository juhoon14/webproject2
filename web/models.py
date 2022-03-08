from django.db import models

# Create your models here.
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_pwd = models.CharField(max_length=10)
#     user_name = models.CharField(max_length=20)
#     user_phone = models.CharField(max_length=50)
#     user_email = models.CharField(max_length=50)
#     user_address = models.CharField(max_length=50)
#     class Meta:
#         db_table = 'User'
#
# class Item(models.Model):
#     product_number = models.AutoField(primary_key=True)
#     key2 = models.IntegerField()
#     product_name = models.CharField(max_length=50, blank=True, null=True)
#     product_img = models.CharField(max_length=50, blank=True, null=True)
#     product_price = models.IntegerField()
#     product_stock = models.IntegerField()
#     product_desc = models.CharField(max_length=50, blank=True, null=True)
#     product_date = models.DateField(auto_now=True)
#     product_hits = models.IntegerField()
#
#     class Meta:
#         db_table = 'Item'
#
# class Orderr(models.Model):
#     order_number = models.AutoField(primary_key=True);
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
#     order_status = models.CharField(max_length=30)
#     order_date = models.DateField(auto_now=True);
#
#     class Meta:
#         db_table = 'Orderr'
#
# class Order_detail(models.Model):
#     order_detail_number = models.CharField(primary_key=True, max_length=5)
#     product_number = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='product_number')
#     order_number = models.ForeignKey(Orderr, on_delete=models.CASCADE, related_name='order_number')
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
#     order_detail_name = models.CharField(max_length=20)
#     order_detail_address = models.CharField(max_length=100)
#     order_detail_phone = models.CharField(max_length=20)
#
#     class Meta:
#         db_table = 'Order_detail'
#
# class Cart(models.Model):
#     cart_number = models.AutoField(primary_key=True)
#     item_number = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='product_number')
#     user_id = models.IntegerField(blank=True, null=True)
#     product_count = models.DateField(auto_now=True)
#
#     class Meta:
#         db_table = 'Cart'
#
# class Category(models.Model):
#     category_code = models.AutoField(primary_key=True)
#     category_code2 = models.IntegerField(blank=True, null=True)
#     category_name = models.CharField(max_length=30)
#
#     class Meta:
#         db_table = 'Category'