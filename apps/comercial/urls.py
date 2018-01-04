from django.conf.urls import include, url
from apps.comercial.views import (CliLista, CliNuevo, CliView, CliEdita, CliDelet,
                                  PrvLista, PrvNuevo, PrvView, PrvEdita, PrvDelet,
                                  VndLista, VndNuevo, VndView, VndEdita, VndDelet,
                                  MviLista, MviNuevo, MviView, MviEdita, MviDelet,
                                  PedLista, PedNuevo, PedView, PedEdita, PedDelet, PedRepor,
                                  FacLista, FacPrint, FacNuevo, FacView, FacEdita, FacPaid, FacDelet)
from apps.inventarios.views import PopExist

urlpatterns = [
    url(r'^CliPanel',                  CliLista.as_view(), name='cli_panel'),
    url(r'^CliNuevo/$',                CliNuevo.as_view(), name='cli_new'),
    url(r'^CliConsulta/(?P<pk>\d+)/$', CliView.as_view(),  name='cli_view'),
    url(r'^CliEdita/(?P<pk>\d+)/$',    CliEdita.as_view(), name='cli_edit'),
    url(r'^CliElimina/(?P<pk>\d+)/$',  CliDelet.as_view(), name='cli_delet'),

    url(r'^PrvPanel',                  PrvLista.as_view(), name='prv_panel'),
    url(r'^PrvNuevo/$',                PrvNuevo.as_view(), name='prv_new'),
    url(r'^PrvConsulta/(?P<pk>\d+)/$', PrvView.as_view(),  name='prv_view'),
    url(r'^PrvEdita/(?P<pk>\d+)/$',    PrvEdita.as_view(), name='prv_edit'),
    url(r'^PrvElimina/(?P<pk>\d+)/$',  PrvDelet.as_view(), name='prv_delet'),

    url(r'^VndPanel',                  VndLista.as_view(), name='vnd_panel'),
    url(r'^VndNuevo/$',                VndNuevo.as_view(), name='vnd_new'),
    url(r'^VndConsulta/(?P<pk>\d+)/$', VndView.as_view(),  name='vnd_view'),
    url(r'^VndEdita/(?P<pk>\d+)/$',    VndEdita.as_view(), name='vnd_edit'),
    url(r'^VndElimina/(?P<pk>\d+)/$',  VndDelet.as_view(), name='vnd_delet'),

    url(r'^MviPanel',                  MviLista.as_view(), name='mvi_panel'),
    url(r'^MviNuevo/$',                MviNuevo.as_view(), name='mvi_new'),
    url(r'^MviConsulta/(?P<pk>\d+)/$', MviView.as_view(),  name='mvi_view'),
    url(r'^MviEdita/(?P<pk>\d+)/$',    MviEdita.as_view(), name='mvi_edit'),
    url(r'^MviElimina/(?P<pk>\d+)/$',  MviDelet.as_view(), name='mvi_delet'),

    url(r'^PopProdc',                  PopExist.as_view(), name='pop_exist'),
    url(r'^PedPanel',                  PedLista.as_view(), name='ped_panel'),
    url(r'^PedNuevo/$',                PedNuevo.as_view(), name='ped_new'),
    url(r'^PedRepor',                  PedRepor.as_view(), name='ped_repor'),
    url(r'^PedConsulta/(?P<pk>\d+)/$', PedView.as_view(),  name='ped_view'),
    url(r'^PedEdita/(?P<pk>\d+)/$',    PedEdita.as_view(), name='ped_edit'),
    url(r'^PedElimina/(?P<pk>\d+)/$',  PedDelet.as_view(), name='ped_delet'),

    url(r'^FacPanel',                  FacLista.as_view(), name='fac_panel'),
    url(r'^FacNuevo/$',                FacNuevo.as_view(), name='fac_new'),
    url(r'^FacPaid/(?P<pk>\d+)/$',     FacPaid.as_view(), name='fac_paid'),
    url(r'^FacConsulta/(?P<pk>\d+)/$', FacView.as_view(),  name='fac_view'),
    url(r'^FacEdita/(?P<pk>\d+)/$',    FacEdita.as_view(), name='fac_edit'),
    url(r'^FacElimina/(?P<pk>\d+)/$',  FacDelet.as_view(), name='fac_delet'),
    url(r'^FacPrint/(?P<pk>\d+)/$',    FacPrint.as_view(), name='fac_print'),

]

#if settings.DEBUG:
#	urlpatterns += [
#		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}
#			),
#	]
