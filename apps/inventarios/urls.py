from django.conf.urls import include, url
#from django.conf.urls import url
from .views import (ExiLista, ExiNuevo, ExiView, ExiEdita, ExiDelet, SxtLista,
                    DivLista, DivNuevo, DivView, DivEdita, DivDelet, MrkLista,
                    MrkNuevo, MrkView, MrkEdita, MrkDelet, ModLista, ModNuevo,
                    ModView, ModEdita, ModDelet, ColLista, ColNuevo, ColView,
                    ColEdita, ColDelet, TllLista, TllNuevo, TllView, TllEdita,
                    TllDelet, Mrkkyselect)

#from django.conf import settings

#from apps.parametros.views import  CliLista, PrvLista, VndLista, MviLista, PedLista, FacLista
#from apps.parametros.views import  CjaLista, CjrLista, McjLista, MdaLista
#SucNuevo, SucView, SucEdita, SucDelet
urlpatterns = [

#    url(r'^PrdPanel',                  PrdLista.as_view(), name='prd_panel'),
#    url(r'^PrdNuevo/$',                PrdNuevo.as_view(), name='prd_new'),
#    url(r'^PrdConsulta/(?P<pk>\d+)/$', PrdView.as_view(),  name='prd_view'),
#    url(r'^PrdEdita/(?P<pk>\d+)/$',    PrdEdita.as_view(), name='prd_edit'),
#    url(r'^PrdElimina/(?P<pk>\d+)/$',  PrdDelet.as_view(), name='prd_delet'),

    url(r'^DivPanel',                  DivLista.as_view(), name='div_panel'),
    url(r'^DivNuevo/$',                DivNuevo.as_view(), name='div_new'),
    url(r'^DivConsulta/(?P<pk>\d+)/$', DivView.as_view(),  name='div_view'),
    url(r'^DivEdita/(?P<pk>\d+)/$',    DivEdita.as_view(), name='div_edit'),
    url(r'^DivElimina/(?P<pk>\d+)/$',  DivDelet.as_view(), name='div_delet'),

    url(r'^MrkPanel',                  MrkLista.as_view(), name='mrk_panel'),
    url(r'^MrkNuevo/$',                MrkNuevo.as_view(), name='mrk_new'),
    url(r'^MrkConsulta/(?P<pk>\d+)/$', MrkView.as_view(),  name='mrk_view'),
    url(r'^MrkEdita/(?P<pk>\d+)/$',    MrkEdita.as_view(), name='mrk_edit'),
    url(r'^MrkElimina/(?P<pk>\d+)/$',  MrkDelet.as_view(), name='mrk_delet'),

    url(r'^ModPanel',                  ModLista.as_view(), name='mod_panel'),
    url(r'^ModNuevo/$',                ModNuevo.as_view(), name='mod_new'),
    url(r'^ModConsulta/(?P<pk>\d+)/$', ModView.as_view(),  name='mod_view'),
    url(r'^ModEdita/(?P<pk>\d+)/$',    ModEdita.as_view(), name='mod_edit'),
    url(r'^ModElimina/(?P<pk>\d+)/$',  ModDelet.as_view(), name='mod_delet'),

    url(r'^ColPanel',                  ColLista.as_view(), name='col_panel'),
    url(r'^ColNuevo/$',                ColNuevo.as_view(), name='col_new'),
    url(r'^ColConsulta/(?P<pk>\d+)/$', ColView.as_view(),  name='col_view'),
    url(r'^ColEdita/(?P<pk>\d+)/$',    ColEdita.as_view(), name='col_edit'),
    url(r'^ColElimina/(?P<pk>\d+)/$',  ColDelet.as_view(), name='col_delet'),

    url(r'^TllPanel',                  TllLista.as_view(), name='tll_panel'),
    url(r'^TllNuevo/$',                TllNuevo.as_view(), name='tll_new'),
    url(r'^TllConsulta/(?P<pk>\d+)/$', TllView.as_view(),  name='tll_view'),
    url(r'^TllEdita/(?P<pk>\d+)/$',    TllEdita.as_view(), name='tll_edit'),
    url(r'^TllElimina/(?P<pk>\d+)/$',  TllDelet.as_view(), name='tll_delet'),

     url(r'^ExiPanel',                  ExiLista.as_view(), name='exi_panel'),
     url(r'^ExiNuevo/$',                ExiNuevo.as_view(), name='exi_new'),
#    url(r'^ExiConsulta/(?P<pk>\d+)/$', ExiView.as_view(),  name='exi_view'),
#    url(r'^ExiEdita/(?P<pk>\d+)/$',    ExiEdita.as_view(), name='exi_edit'),
#    url(r'^ExiElimina/(?P<pk>\d+)/$',  ExiDelet.as_view(), name='exi_delet'),

#    url(r'^SxtPanel',                  SxtLista.as_view(), name='sxt_panel'),
#    url(r'^SxtNuevo/$',                SxtNuevo.as_view(), name='sxt_new'),
#    url(r'^SxtConsulta/(?P<pk>\d+)/$', SxtView.as_view(),  name='sxt_view'),
#    url(r'^SxtEdita/(?P<pk>\d+)/$',    SxtEdita.as_view(), name='sxt_edit'),
#    url(r'^SxtElimina/(?P<pk>\d+)/$',  SxtDelet.as_view(), name='sxt_delet'),

#    url(r'^CliPanel',                  CliLista.as_view(), name='cli_panel'),
#    url(r'^CliNuevo/$',                CliNuevo.as_view(), name='cli_new'),
#    url(r'^CliConsulta/(?P<pk>\d+)/$', CliView.as_view(),  name='cli_view'),
#    url(r'^CliEdita/(?P<pk>\d+)/$',    CliEdita.as_view(), name='cli_edit'),
#    url(r'^CliElimina/(?P<pk>\d+)/$',  CliDelet.as_view(), name='cli_delet'),

#    url(r'^PrvPanel',                  PrvLista.as_view(), name='prv_panel'),
#    url(r'^PrvNuevo/$',                PrvNuevo.as_view(), name='prv_new'),
#    url(r'^PrvConsulta/(?P<pk>\d+)/$', PrvView.as_view(),  name='prv_view'),
#    url(r'^PrvEdita/(?P<pk>\d+)/$',    PrvEdita.as_view(), name='prv_edit'),
#    url(r'^PrvElimina/(?P<pk>\d+)/$',  PrvDelet.as_view(), name='prv_delet'),

#    url(r'^VndPanel',                  VndLista.as_view(), name='vnd_panel'),
#    url(r'^VndNuevo/$',                VndNuevo.as_view(), name='vnd_new'),
#    url(r'^VndConsulta/(?P<pk>\d+)/$', VndView.as_view(),  name='vnd_view'),
#    url(r'^VndEdita/(?P<pk>\d+)/$',    VndEdita.as_view(), name='vnd_edit'),
#    url(r'^VndElimina/(?P<pk>\d+)/$',  VndDelet.as_view(), name='vnd_delet'),

#    url(r'^MviPanel',                  MviLista.as_view(), name='mvi_panel'),
#    url(r'^MviNuevo/$',                MviNuevo.as_view(), name='mvi_new'),
#    url(r'^MviConsulta/(?P<pk>\d+)/$', MviView.as_view(),  name='mvi_view'),
#    url(r'^MviEdita/(?P<pk>\d+)/$',    MviEdita.as_view(), name='mvi_edit'),
#    url(r'^MviElimina/(?P<pk>\d+)/$',  MviDelet.as_view(), name='mvi_delet'),

#    url(r'^PedPanel',                  PedLista.as_view(), name='ped_panel'),
#    url(r'^PedNuevo/$',                PedNuevo.as_view(), name='ped_new'),
#    url(r'^PedConsulta/(?P<pk>\d+)/$', PedView.as_view(),  name='ped_view'),
#    url(r'^PedEdita/(?P<pk>\d+)/$',    PedEdita.as_view(), name='ped_edit'),
#    url(r'^PedElimina/(?P<pk>\d+)/$',  PedDelet.as_view(), name='ped_delet'),

#    url(r'^FacPanel',                  FacLista.as_view(), name='fac_panel'),
#    url(r'^FacNuevo/$',                FacNuevo.as_view(), name='fac_new'),
#    url(r'^FacConsulta/(?P<pk>\d+)/$', FacView.as_view(),  name='fac_view'),
#    url(r'^FacEdita/(?P<pk>\d+)/$',    FacEdita.as_view(), name='fac_edit'),
#    url(r'^FacElimina/(?P<pk>\d+)/$',  FacDelet.as_view(), name='fac_delet'),

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
#   urlpatterns += [
#       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}
#           ),
#   ]
