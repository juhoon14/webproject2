from django_request_mapping import UrlPattern
from web.views import MyView
from web.views_cust import custcenView
from web.views_item import ItemView
from web.views_user import UserView

urlpatterns = UrlPattern()
urlpatterns.register(MyView)
urlpatterns.register(UserView)
urlpatterns.register(ItemView)
urlpatterns.register(custcenView)