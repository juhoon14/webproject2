from django_request_mapping import UrlPattern

from web.views import MyView
from web.views_itemadd import itemView

urlpatterns = UrlPattern();
urlpatterns.register(MyView);
urlpatterns.register(itemView)