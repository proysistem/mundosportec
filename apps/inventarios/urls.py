from django.conf.urls import include, url
#from django.conf.urls import url
from .views import (ExiLista, ExiNuevo, ExiView, ExiEdita, ExiDelet, SxtLista, ExiPrint,
                    DivLista, DivNuevo, DivView, DivEdita, DivDelet, MrkLista,
                    MrkNuevo, MrkView, MrkEdita, MrkDelet, ModLista, ModNuevo,
                    ModView, ModEdita, ModDelet, ColLista, ColNuevo, ColView,
                    ColEdita, ColDelet, TllLista, TllNuevo, TllView, TllEdita,
                    TllDelet, Mrkkyselect, TablaTalla, PopTalla)


#from django.conf import settings

#from apps.parametros.views import  CliLista, PrvLista, VndLista, MviLista, PedLista, FacLista
#from apps.parametros.views import  CjaLista, CjrLista, McjLista, MdaLista
#SucNuevo, SucView, SucEdita, SucDelet
urlpatterns = [
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
    url(r'^TllConsulta/(?P<pk>\w+)/$', TllView.as_view(),  name='tll_view'),
    url(r'^TllEdita/(?P<pk>\w+)/$',    TllEdita.as_view(), name='tll_edit'),
    url(r'^TllElimina/(?P<pk>\w+)/$',  TllDelet.as_view(), name='tll_delet'),
    url(r'^TllPopup/(?P<pk>\d+)/$',    PopTalla.as_view(), name='pop_talla'),

    url(r'^ExiPanel',                  ExiLista.as_view(), name='exi_panel'),
    url(r'^ExiPrint',                  ExiPrint.as_view(), name='exi_print'),
    url(r'^ExiNuevo/$',                ExiNuevo.as_view(), name='exi_new'),
    url(r'^ExiEdita/(?P<pk>\d+)/$',    ExiEdita.as_view(), name='exi_edit'),
    url(r'^TablaTalla/(?P<model>\d+)/$',  TablaTalla.as_view(), name='tabla_talla'),
    #   url(r'^ExiNuevo/$',                ProdkyLista.as_view(), name='exi_new'),
    url(r'^ExiConsulta/(?P<pk>\d+)/$', ExiView.as_view(),  name='exi_view'),
    #   url(r'^ExiElimina/(?P<pk>\d+)/$',  ExiDelet.as_view(), name='exi_delet'),

    #   url(r'^SxtPanel',                  SxtLista.as_view(), name='sxt_panel'),
    #   url(r'^SxtNuevo/$',                SxtNuevo.as_view(), name='sxt_new'),
    #   url(r'^SxtConsulta/(?P<pk>\d+)/$', SxtView.as_view(),  name='sxt_view'),
    #   url(r'^SxtEdita/(?P<pk>\d+)/$',    SxtEdita.as_view(), name='sxt_edit'),
    #   url(r'^SxtElimina/(?P<pk>\d+)/$',  SxtDelet.as_view(), name='sxt_delet'),

]

#if settings.DEBUG:
#   urlpatterns += [
#       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}
#           ),
#   ]
