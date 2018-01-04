# from django.conf.urls import patterns, include, url
from django.conf.urls import url
from apps.parametros.views import (SucLista, SucNuevo, SucView, SucEdita, SucDelet,
                                   ZipLista, ZipNuevo, ZipView, ZipEdita, ZipDelet,
                                   PaiLista, PaiNuevo, PaiView, PaiEdita, PaiDelet,
                                   PviLista, PviNuevo, PviView, PviEdita, PviDelet,
                                   CiuLista, CiuNuevo, CiuView, CiuEdita, CiuDelet)

from django.conf import settings

# from apps.parametros.views import  CliLista, PrvLista, VndLista, MviLista, PedLista, FacLista
# from apps.parametros.views import  CjaLista, CjrLista, McjLista, MdaLista
# from apps.parametros.views import  PrdLista, ExiLista, PrcLista, SxtLista, DivLista, MrkLista, ModLista, ColLista, TllLista
# SucNuevo, SucView, SucEdita, SucDelet


urlpatterns = [
    url(r'^SucPanel', 				   SucLista.as_view(), name='suc_panel'),
    url(r'^SucNuevo/$', 			   SucNuevo.as_view(), name='suc_new'),
    url(r'^SucConsulta/(?P<pk>\d+)/$', SucView.as_view(),  name='suc_view'),
    url(r'^SucEdita/(?P<pk>\d+)/$',    SucEdita.as_view(), name='suc_edit'),
    url(r'^SucElimina/(?P<pk>\d+)/$',  SucDelet.as_view(), name='suc_delet'),

    url(r'^ZipPanel',                  ZipLista.as_view(), name='zip_panel'),
    url(r'^ZipNuevo/$',				   ZipNuevo.as_view(), name='zip_new'),
    url(r'^ZipConsulta/(?P<pk>\d+)/$', ZipView.as_view(),  name='zip_view'),
    url(r'^ZipEdita/(?P<pk>\d+)/$',    ZipEdita.as_view(), name='zip_edit'),
    url(r'^ZipElimina/(?P<pk>\d+)/$',  ZipDelet.as_view(), name='zip_delet'),

    url(r'^CiuPanel', 				   CiuLista.as_view(), name='ciu_panel'),
    url(r'^CiuNuevo/$',                CiuNuevo.as_view(), name='ciu_new'),
    url(r'^CiuConsulta/(?P<pk>\d+)/$', CiuView.as_view(),  name='ciu_view'),
    url(r'^CiuEdita/(?P<pk>\d+)/$',    CiuEdita.as_view(), name='ciu_edit'),
    url(r'^CiuElimina/(?P<pk>\d+)/$',  CiuDelet.as_view(), name='ciu_delet'),

    url(r'^PviPanel', 				   PviLista.as_view(), name='pvi_panel'),
    url(r'^PviNuevo/$',                PviNuevo.as_view(), name='pvi_new'),
    url(r'^PviConsulta/(?P<pk>\d+)/$', PviView.as_view(),  name='pvi_view'),
    url(r'^PviEdita/(?P<pk>\d+)/$',    PviEdita.as_view(), name='pvi_edit'),
    url(r'^PviElimina/(?P<pk>\d+)/$',  PviDelet.as_view(), name='pvi_delet'),

    url(r'^PaiPanel', 				   PaiLista.as_view(), name='pai_panel'),
    url(r'^PaiNuevo/$', 			   PaiNuevo.as_view(), name='pai_new'),
    url(r'^PaiConsulta/(?P<pk>\d+)/$', PaiView.as_view(),  name='pai_view'),
    url(r'^PaiEdita/(?P<pk>\d+)/$',    PaiEdita.as_view(), name='pai_edit'),
    url(r'^PaiElimina/(?P<pk>\d+)/$',  PaiDelet.as_view(), name='pai_delet'),

#    url(r'^MdaPanel',                  MdaLista.as_view(), name='mda_panel'),
#    url(r'^MdaNuevo/$',                MdaNuevo.as_view(), name='mda_new'),
#    url(r'^MdaConsulta/(?P<pk>\d+)/$', MdaView.as_view(),  name='mda_view'),
#    url(r'^MdaEdita/(?P<pk>\d+)/$',    MdaEdita.as_view(), name='mda_edit'),
#    url(r'^MdaElimina/(?P<pk>\d+)/$',  MdaDelet.as_view(), name='mda_delet'),

#    url(r'^CjrPanel',                  CjrLista.as_view(), name='cjr_panel'),
#    url(r'^CjrNuevo/$',                CjrNuevo.as_view(), name='cjr_new'),
#    url(r'^CjrConsulta/(?P<pk>\d+)/$', CjrView.as_view(),  name='cjr_view'),
#    url(r'^CjrEdita/(?P<pk>\d+)/$',    CjrEdita.as_view(), name='cjr_edit'),
#    url(r'^CjrElimina/(?P<pk>\d+)/$',  CjrDelet.as_view(), name='cjr_delet'),

#    url(r'^CjaPanel',                  CjaLista.as_view(), name='cja_panel'),
#    url(r'^CjaNuevo/$',                CjaNuevo.as_view(), name='cja_new'),
#    url(r'^CjaConsulta/(?P<pk>\d+)/$', CjaView.as_view(),  name='cja_view'),
#    url(r'^CjaEdita/(?P<pk>\d+)/$',    CjaEdita.as_view(), name='cja_edit'),
#    url(r'^CjaElimina/(?P<pk>\d+)/$',  CjaDelet.as_view(), name='cja_delet'),

#    url(r'^McjPanel',                  McjLista.as_view(), name='mcj_panel'),
#    url(r'^McjNuevo/$',                McjNuevo.as_view(), name='mcj_new'),
#    url(r'^McjConsulta/(?P<pk>\d+)/$', McjView.as_view(),  name='mcj_view'),
#    url(r'^McjEdita/(?P<pk>\d+)/$',    McjEdita.as_view(), name='mcj_edit'),
#    url(r'^McjElimina/(?P<pk>\d+)/$',  McjDelet.as_view(), name='mcj_delet'),
##    url(r'^Nuevo/$', crear_sucursal, name='suc_new'),
##    url(r'^sucursal/$', SucursView.as_view(), name='VerSucursal'),

]

#if settings.DEBUG:
#	urlpatterns += [
#		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}
#			),
#	]
