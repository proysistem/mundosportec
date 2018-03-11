# from django.conf.urls import patterns, include, url
from django.conf.urls import url
from apps.parametros.views import (SucLista, SucNuevo, SucView, SucEdita, SucDelet,
                                   ZipLista, ZipNuevo, ZipView, ZipEdita, ZipDelet,
                                   PaiLista, PaiNuevo, PaiView, PaiEdita, PaiDelet,
                                   PviLista, PviNuevo, PviView, PviEdita, PviDelet,
                                   CiuLista, CiuNuevo, CiuView, CiuEdita, CiuDelet)

from django.conf import settings
from mundosport.utils import login_required_view


# from apps.parametros.views import  CliLista, PrvLista, VndLista, MviLista, PedLista, FacLista
# from apps.parametros.views import  CjaLista, CjrLista, McjLista, MdaLista
# from apps.parametros.views import  PrdLista, ExiLista, PrcLista, SxtLista, DivLista, MrkLista, ModLista, ColLista, TllLista
# SucNuevo, SucView, SucEdita, SucDelet


urlpatterns = [
    url(r'^SucPanel',                  login_required_view(SucLista.as_view()), name='suc_panel'),
    url(r'^SucNuevo/$',                login_required_view(SucNuevo.as_view()), name='suc_new'),
    url(r'^SucConsulta/(?P<pk>\d+)/$', login_required_view(SucView.as_view()),  name='suc_view'),
    url(r'^SucEdita/(?P<pk>\d+)/$',    login_required_view(SucEdita.as_view()), name='suc_edit'),
    url(r'^SucElimina/(?P<pk>\d+)/$',  login_required_view(SucDelet.as_view()), name='suc_delet'),

    url(r'^ZipPanel',                  login_required_view(ZipLista.as_view()), name='zip_panel'),
    url(r'^ZipNuevo/$',                login_required_view(ZipNuevo.as_view()), name='zip_new'),
    url(r'^ZipConsulta/(?P<pk>\d+)/$', login_required_view(ZipView.as_view()),  name='zip_view'),
    url(r'^ZipEdita/(?P<pk>\d+)/$',    login_required_view(ZipEdita.as_view()), name='zip_edit'),
    url(r'^ZipElimina/(?P<pk>\d+)/$',  login_required_view(ZipDelet.as_view()), name='zip_delet'),

    url(r'^CiuPanel',                  login_required_view(CiuLista.as_view()), name='ciu_panel'),
    url(r'^CiuNuevo/$',                login_required_view(CiuNuevo.as_view()), name='ciu_new'),
    url(r'^CiuConsulta/(?P<pk>\d+)/$', login_required_view(CiuView.as_view()),  name='ciu_view'),
    url(r'^CiuEdita/(?P<pk>\d+)/$',    login_required_view(CiuEdita.as_view()), name='ciu_edit'),
    url(r'^CiuElimina/(?P<pk>\d+)/$',  login_required_view(CiuDelet.as_view()), name='ciu_delet'),

    url(r'^PviPanel',                  login_required_view(PviLista.as_view()), name='pvi_panel'),
    url(r'^PviNuevo/$',                login_required_view(PviNuevo.as_view()), name='pvi_new'),
    url(r'^PviConsulta/(?P<pk>\d+)/$', login_required_view(PviView.as_view()),  name='pvi_view'),
    url(r'^PviEdita/(?P<pk>\d+)/$',    login_required_view(PviEdita.as_view()), name='pvi_edit'),
    url(r'^PviElimina/(?P<pk>\d+)/$',  login_required_view(PviDelet.as_view()), name='pvi_delet'),

    url(r'^PaiPanel',                  login_required_view(PaiLista.as_view()), name='pai_panel'),
    url(r'^PaiNuevo/$',                login_required_view(PaiNuevo.as_view()), name='pai_new'),
    url(r'^PaiConsulta/(?P<pk>\d+)/$', login_required_view(PaiView.as_view()),  name='pai_view'),
    url(r'^PaiEdita/(?P<pk>\d+)/$',    login_required_view(PaiEdita.as_view()), name='pai_edit'),
    url(r'^PaiElimina/(?P<pk>\d+)/$',  login_required_view(PaiDelet.as_view()), name='pai_delet'),
    ]
