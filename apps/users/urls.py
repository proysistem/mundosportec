from django.conf.urls import url, include
from apps.users.views import UsrNuevo

urlpatterns = [
    url(r'^UsrNuevo/$', UsrNuevo.as_view(),  name="usr_new"),
    # url(r'^login/$', 'apps.users.views.Userlogin',  name="login"),
]
