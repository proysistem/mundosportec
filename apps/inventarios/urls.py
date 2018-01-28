from django.conf.urls import include, url
# from django.conf.urls import url
from .views import (ExiLista, ExiNuevo, ExiView, ExiEdita, ExiDelet, SxtLista, ExiPrint, ExiQuery, ExiTiket,
                    DivLista, DivNuevo, DivView, DivEdita, DivDelet, MrkLista,
                    MrkNuevo, MrkView, MrkEdita, MrkDelet, ModLista, ModNuevo,
                    ModView, ModEdita, ModDelet, ColLista, ColNuevo, ColView,
                    ColEdita, ColDelet, TllLista, TllNuevo, TllView, TllEdita,
                    TllDelet, Mrkkyselect, TablaTalla, PopTalla)
from mundosport.utils import login_required_view

# from django.conf import settings

# from apps.parametros.views import  CliLista, PrvLista, VndLista, MviLista, PedLista, FacLista
# from apps.parametros.views import  CjaLista, CjrLista, McjLista, MdaLista
# SucNuevo, SucView, SucEdita, SucDelet



urlpatterns = [
    url(r'^DivPanel',                  login_required_view(DivLista.as_view()), name='div_panel'),
    url(r'^DivNuevo/$',                login_required_view(DivNuevo.as_view()), name='div_new'),
    url(r'^DivConsulta/(?P<pk>\d+)/$', login_required_view(DivView.as_view()),  name='div_view'),
    url(r'^DivEdita/(?P<pk>\d+)/$',    login_required_view(DivEdita.as_view()), name='div_edit'),
    url(r'^DivElimina/(?P<pk>\d+)/$',  login_required_view(DivDelet.as_view()), name='div_delet'),

    url(r'^MrkPanel',                  login_required_view(MrkLista.as_view()), name='mrk_panel'),
    url(r'^MrkNuevo/$',                login_required_view(MrkNuevo.as_view()), name='mrk_new'),
    url(r'^MrkConsulta/(?P<pk>\d+)/$', login_required_view(MrkView.as_view()),  name='mrk_view'),
    url(r'^MrkEdita/(?P<pk>\d+)/$',    login_required_view(MrkEdita.as_view()), name='mrk_edit'),
    url(r'^MrkElimina/(?P<pk>\d+)/$',  login_required_view(MrkDelet.as_view()), name='mrk_delet'),

    url(r'^ModPanel',                  login_required_view(ModLista.as_view()), name='mod_panel'),
    url(r'^ModNuevo/$',                login_required_view(ModNuevo.as_view()), name='mod_new'),
    url(r'^ModConsulta/(?P<pk>\d+)/$', login_required_view(ModView.as_view()),  name='mod_view'),
    url(r'^ModEdita/(?P<pk>\d+)/$',    login_required_view(ModEdita.as_view()), name='mod_edit'),
    url(r'^ModElimina/(?P<pk>\d+)/$',  login_required_view(ModDelet.as_view()), name='mod_delet'),

    url(r'^ColPanel',                  login_required_view(ColLista.as_view()), name='col_panel'),
    url(r'^ColNuevo/$',                login_required_view(ColNuevo.as_view()), name='col_new'),
    url(r'^ColConsulta/(?P<pk>\d+)/$', login_required_view(ColView.as_view()),  name='col_view'),
    url(r'^ColEdita/(?P<pk>\d+)/$',    login_required_view(ColEdita.as_view()), name='col_edit'),
    url(r'^ColElimina/(?P<pk>\d+)/$',  login_required_view(ColDelet.as_view()), name='col_delet'),

    url(r'^TllPanel',                  login_required_view(TllLista.as_view()), name='tll_panel'),
    url(r'^TllNuevo/$',                login_required_view(TllNuevo.as_view()), name='tll_new'),
    url(r'^TllConsulta/(?P<pk>\w+)/$', login_required_view(TllView.as_view()),  name='tll_view'),
    url(r'^TllEdita/(?P<pk>\w+)/$',    login_required_view(TllEdita.as_view()), name='tll_edit'),
    url(r'^TllElimina/(?P<pk>\w+)/$',  login_required_view(TllDelet.as_view()), name='tll_delet'),
    url(r'^TllPopup/(?P<pk>\d+)/$',    login_required_view(PopTalla.as_view()), name='pop_talla'),

    url(r'^ExiPanel',                  login_required_view(ExiLista.as_view()), name='exi_panel'),
    url(r'^ExiPrint',                  login_required_view(ExiPrint.as_view()), name='exi_print'),
    url(r'^ExiTiket',                  login_required_view(ExiTiket.as_view()), name='exi_tiket'),
    url(r'^ExiNuevo/$',                login_required_view(ExiNuevo.as_view()), name='exi_new'),
    url(r'^ExiEdita/(?P<pk>\d+)/$',    login_required_view(ExiEdita.as_view()), name='exi_edit'),
    url(r'^ExiQuery/(?P<exs_product>\d+)/$',    login_required_view(ExiQuery.as_view()), name='exi_query'),
    url(r'^TablaTalla/(?P<model>\d+)/$',  login_required_view(TablaTalla.as_view()), name='tabla_talla'),
    #   url(r'^ExiNuevo/$',                ProdkyLista.as_view(), name='exi_new'),
    url(r'^ExiConsulta/(?P<pk>\d+)/$', login_required_view(ExiView.as_view()),  name='exi_view'),
    url(r'^ExiElimina/(?P<pk>\d+)/$',  login_required_view(ExiDelet.as_view()), name='exi_delet'),

]
