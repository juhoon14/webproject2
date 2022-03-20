from django.conf import settings
from django.db import models

from config import settings


class Cart(models.Model):
    cart_number = models.AutoField(primary_key=True)
    u = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    p_number = models.ForeignKey('Item', models.DO_NOTHING, db_column='p_number', blank=True, null=True)
    product_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Category(models.Model):
    category_code = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Item(models.Model):
    product_number = models.AutoField(primary_key=True)
    c_code = models.ForeignKey(Category, models.DO_NOTHING, db_column='c_code', blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    product_price = models.CharField(max_length=15, blank=True, null=True)
    product_img = models.CharField(max_length=50, blank=True, null=True)
    product_desc = models.TextField(blank=True, null=True)
    product_desc_img = models.CharField(max_length=50, blank=True, null=True)
    product_s_size = models.IntegerField(blank=True, null=True)
    product_m_size = models.IntegerField(blank=True, null=True)
    product_l_size = models.IntegerField(blank=True, null=True)
    product_xl_size = models.IntegerField(blank=True, null=True)
    product_hits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'

class ItemQna(models.Model):
    qna_number = models.AutoField(primary_key=True)
    p_number = models.ForeignKey(Item, models.DO_NOTHING, db_column='p_number', blank=True, null=True)
    u = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    u_pwd = models.CharField(max_length=50, blank=True, null=True)
    qna_title = models.CharField(max_length=50, blank=True, null=True)
    qna_desc = models.TextField(blank=True, null=True)
    qna_date = models.DateField(blank=True, null=True)
    qna_state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_qna'

class MainQna(models.Model):
    m_qna_number = models.AutoField(primary_key=True)
    u = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    u_pwd = models.CharField(max_length=50, blank=True, null=True)
    m_qna_title = models.CharField(max_length=50, blank=True, null=True)
    m_qna_desc = models.TextField(blank=True, null=True)
    m_qna_date = models.DateField(blank=True, null=True)
    m_qna_state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_qna'


class OrderDetail(models.Model):
    order_detail_number = models.AutoField(primary_key=True)
    p_number = models.ForeignKey(Item, models.DO_NOTHING, db_column='p_number', blank=True, null=True)
    o_number = models.ForeignKey('Orderr', models.DO_NOTHING, db_column='o_number', blank=True, null=True)
    u = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    order_detail_name = models.CharField(max_length=20, blank=True, null=True)
    order_detail_address = models.CharField(max_length=100, blank=True, null=True)
    order_detail_phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_detail'


class Orderr(models.Model):
    order_number = models.AutoField(primary_key=True)
    u = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    p_number = models.ForeignKey(Item, models.DO_NOTHING, db_column='p_number', blank=True, null=True)
    order_name = models.CharField(max_length=20, blank=True, null=True)
    order_phone = models.CharField(max_length=20, blank=True, null=True)
    order_addr1 = models.CharField(max_length=100, blank=True, null=True)
    order_addr2 = models.CharField(max_length=100, blank=True, null=True)
    order_msg = models.TextField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    order_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderr'

class Review(models.Model):
    review_number = models.AutoField(primary_key=True)
    p_number = models.ForeignKey(Item, models.DO_NOTHING, db_column='p_number', blank=True, null=True)
    u = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    review_img = models.CharField(max_length=50, blank=True, null=True)
    review_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30)
    user_pwd = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    user_phone = models.CharField(max_length=20, blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    user_address1 = models.CharField(max_length=100, blank=True, null=True)
    user_address2 = models.CharField(max_length=100, blank=True, null=True)
    user_auth = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
