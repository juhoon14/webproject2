from django_request_mapping import UrlPattern
from web.views import MyView
from web.views_item import ItemView
# from web.views_top import TopView

# from web.views_bottom import BottomView
# from web.views_bottom import BottomView
# from web.views_top import TopView
from web.views_user import UserView

urlpatterns = UrlPattern()
urlpatterns.register(MyView)
# urlpatterns.register(TopView)
# urlpatterns.register(BottomView)
urlpatterns.register(ItemView)
urlpatterns.register(UserView)