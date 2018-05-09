from django.conf.urls import url
from apps.comercial.views import (CliLista, CliNuevo, CliView, CliEdita, CliDelet,
                                  PrvLista, PrvNuevo, PrvView, PrvEdita, PrvDelet,
                                  VndLista, VndNuevo, VndView, VndEdita, VndDelet,
                                  MviLista, MviNuevo, MviView, MviEdita, MviDelet,
                                  PedLista, PedNuevo, PedView, PedEdita, PedDelet, PedRepor,
                                  FacLista, FacPrint, FacNuevo, FacView, FacEdita, FacPaid, FacDelet, FacBuscar,
                                  IngNuevo, IngEdita,
                                  ComNuevo, ComLista, ComBuscar, ComView, ComPrint,
                                  MviBuscar,
                                  AjcLista, AjcNuevo, AjcRepor, AjcView, AjcEdita, AjcDelet,
                                  NcrBuscar, NcrLista, NcrNuevo, NcrView, NcrEdita, NcrDelet, NcrPrint)
from apps.inventarios.views import PopExist
from mundosport.utils import login_required_view


urlpatterns = [
    url(r'^CliPanel',                  login_required_view(CliLista.as_view()), name='cli_panel'),
    url(r'^CliNuevo/$',                login_required_view(CliNuevo.as_view()), name='cli_new'),
    url(r'^CliConsulta/(?P<pk>\d+)/$', login_required_view(CliView.as_view()),  name='cli_view'),
    url(r'^CliEdita/(?P<pk>\d+)/$',    login_required_view(CliEdita.as_view()), name='cli_edit'),
    url(r'^CliElimina/(?P<pk>\d+)/$',  login_required_view(CliDelet.as_view()), name='cli_delet'),

    url(r'^PrvPanel',                  login_required_view(PrvLista.as_view()), name='prv_panel'),
    url(r'^PrvNuevo/$',                login_required_view(PrvNuevo.as_view()), name='prv_new'),
    url(r'^PrvConsulta/(?P<pk>\d+)/$', login_required_view(PrvView.as_view()),  name='prv_view'),
    url(r'^PrvEdita/(?P<pk>\d+)/$',    login_required_view(PrvEdita.as_view()), name='prv_edit'),
    url(r'^PrvElimina/(?P<pk>\d+)/$',  login_required_view(PrvDelet.as_view()), name='prv_delet'),

    url(r'^VndPanel',                  login_required_view(VndLista.as_view()), name='vnd_panel'),
    url(r'^VndNuevo/$',                login_required_view(VndNuevo.as_view()), name='vnd_new'),
    url(r'^VndConsulta/(?P<pk>\d+)/$', login_required_view(VndView.as_view()),  name='vnd_view'),
    url(r'^VndEdita/(?P<pk>\d+)/$',    login_required_view(VndEdita.as_view()), name='vnd_edit'),
    url(r'^VndElimina/(?P<pk>\d+)/$',  login_required_view(VndDelet.as_view()), name='vnd_delet'),

    url(r'^MviSearch',                 login_required_view(MviBuscar.as_view()), name='mvi_search'),
    url(r'^MviPanel',                  login_required_view(MviLista.as_view()), name='mvi_panel'),
    url(r'^MviNuevo/$',                login_required_view(MviNuevo.as_view()), name='mvi_new'),
    url(r'^MviConsulta/(?P<pk>\d+)/$', login_required_view(MviView.as_view()),  name='mvi_view'),
    url(r'^MviEdita/(?P<pk>\d+)/$',    login_required_view(MviEdita.as_view()), name='mvi_edit'),
    url(r'^MviElimina/(?P<pk>\d+)/$',  login_required_view(MviDelet.as_view()), name='mvi_delet'),

    url(r'^PopProdc',                  login_required_view(PopExist.as_view()), name='pop_exist'),
    url(r'^PedPanel',                  login_required_view(PedLista.as_view()), name='ped_panel'),
    url(r'^PedNuevo/$',                login_required_view(PedNuevo.as_view()), name='ped_new'),
    url(r'^PedRepor',                  login_required_view(PedRepor.as_view()), name='ped_repor'),
    url(r'^PedConsulta/(?P<pk>\d+)/$', login_required_view(PedView.as_view()),  name='ped_view'),
    url(r'^PedEdita/(?P<pk>\d+)/$',    login_required_view(PedEdita.as_view()), name='ped_edit'),
    url(r'^PedElimina/(?P<pk>\d+)/$',  login_required_view(PedDelet.as_view()), name='ped_delet'),

    url(r'^IngPanel',                  login_required_view(PedLista.as_view()), name='ing_panel'),
    url(r'^IngNuevo/$',                login_required_view(IngNuevo.as_view()), name='ing_new'),
    url(r'^IngRepor',                  login_required_view(PedRepor.as_view()), name='ing_repor'),
    url(r'^IngConsulta/(?P<pk>\d+)/$', login_required_view(PedView.as_view()),  name='ing_view'),
    url(r'^IngEdita/(?P<pk>\d+)/$',    login_required_view(IngEdita.as_view()), name='ing_edit'),
    url(r'^IngElimina/(?P<pk>\d+)/$',  login_required_view(PedDelet.as_view()), name='ing_delet'),

    url(r'^ComSearch',                 login_required_view(ComBuscar.as_view()), name='com_search'),
    url(r'^ComPanel',                  login_required_view(ComLista.as_view()), name='com_panel'),
    url(r'^ComNuevo/$',                login_required_view(ComNuevo.as_view()), name='com_new'),
    # url(r'^ComPaid/(?P<pk>\d+)/$',     login_required_view(FacPaid.as_view()), name='fac_paid'),
    url(r'^ComConsulta/(?P<pk>\d+)/$', login_required_view(ComView.as_view()),  name='com_view'),
    # url(r'^ComEdita/(?P<pk>\d+)/$',    login_required_view(FacEdita.as_view()), name='fac_edit'),
    # url(r'^ComElimina/(?P<pk>\d+)/$',  login_required_view(FacDelet.as_view()), name='fac_delet'),
    url(r'^ComPrint/(?P<pk>\d+)/$',    login_required_view(ComPrint.as_view()), name='com_print'),

    url(r'^FacSearch',                 login_required_view(FacBuscar.as_view()), name='fac_search'),
    url(r'^FacPanel',                  login_required_view(FacLista.as_view()), name='fac_panel'),
    url(r'^FacNuevo/$',                login_required_view(FacNuevo.as_view()), name='fac_new'),
    url(r'^FacPaid/(?P<pk>\d+)/$',     login_required_view(FacPaid.as_view()), name='fac_paid'),
    url(r'^FacConsulta/(?P<pk>\d+)/$', login_required_view(FacView.as_view()),  name='fac_view'),
    url(r'^FacEdita/(?P<pk>\d+)/$',    login_required_view(FacEdita.as_view()), name='fac_edit'),
    url(r'^FacElimina/(?P<pk>\d+)/$',  login_required_view(FacDelet.as_view()), name='fac_delet'),
    url(r'^FacPrint/(?P<pk>\d+)/$',    login_required_view(FacPrint.as_view()), name='fac_print'),
    url(r'^PopProdc',                  login_required_view(PopExist.as_view()), name='pop_exist'),

    url(r'^AjcPanel',                  login_required_view(AjcLista.as_view()), name='ajc_panel'),
    url(r'^AjcNuevo/$',                login_required_view(AjcNuevo.as_view()), name='ajc_new'),
    url(r'^AjcRepor',                  login_required_view(AjcRepor.as_view()), name='ajc_repor'),
    url(r'^AjcConsulta/(?P<pk>\d+)/$', login_required_view(AjcView.as_view()),  name='ajc_view'),
    url(r'^AjcEdita/(?P<pk>\d+)/$',    login_required_view(AjcEdita.as_view()), name='ajc_edit'),
    url(r'^AjcElimina/(?P<pk>\d+)/$',  login_required_view(AjcDelet.as_view()), name='ajc_delet'),

    url(r'^NcrSearch',                 login_required_view(NcrBuscar.as_view()), name='ncr_search'),
    url(r'^NcrPanel',                  login_required_view(NcrLista.as_view()), name='ncr_panel'),
    url(r'^NcrNuevo/$',                login_required_view(NcrNuevo.as_view()), name='ncr_new'),
    url(r'^NcrConsulta/(?P<pk>\d+)/$', login_required_view(NcrView.as_view()),  name='ncr_view'),
    url(r'^NcrEdita/(?P<pk>\d+)/$',    login_required_view(NcrEdita.as_view()), name='ncr_edit'),
    url(r'^NcrElimina/(?P<pk>\d+)/$',  login_required_view(NcrDelet.as_view()), name='ncr_delet'),
    url(r'^NcrPrint/(?P<pk>\d+)/$',    login_required_view(NcrPrint.as_view()), name='ncr_print'),

]
