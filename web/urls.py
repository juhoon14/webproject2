from django_request_mapping import UrlPattern
from web.views import MyView
from web.views_user import UserView

urlpatterns = UrlPattern()
urlpatterns.register(MyView)
urlpatterns.register(UserView)