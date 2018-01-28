from django.conf.urls import url
from apps.users.views import UsrNuevo
from django.contrib import admin



urlpatterns = [
    url(r'^UsrNuevo/$', UsrNuevo.as_view,  name="usr_new"),
    url(r'^$', 'apps.users.views.users'),
    # url(r'^login/$', 'apps.users.views.Userlogin',  name="login"),
]
