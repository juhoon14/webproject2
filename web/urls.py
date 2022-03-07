from django_request_mapping import UrlPattern

from web.views import MyView
from web.views_top import TopView

from web.views_bottom import BottomView

urlpatterns = UrlPattern();
urlpatterns.register(MyView);
urlpatterns.register(TopView);
urlpatterns.register(BottomView);