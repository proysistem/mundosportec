from django.conf.urls import url

# from apps.inicio.views import IndexView, home

from apps.inicio.views import home


urlpatterns = [
    # url(r'^$', IndexView, name='iniciar'),
    url(r'^$', home, name='home'),
]
