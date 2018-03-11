from django.conf.urls import url
from .views import (CjaLista, CjaNuevo, CjaView, CjaEdita, CjaDelet, CjrLista, CjrNuevo, CjrView, CjrEdita, CjrDelet,
                    McjLista, McjNuevo, McjView, McjEdita, McjDelet, MdaLista, MdaNuevo, MdaView, MdaEdita, MdaDelet)

from mundosport.utils import login_required_view


urlpatterns = [

    url(r'^MdaPanel',                  login_required_view(MdaLista.as_view()), name='mda_panel'),
    url(r'^MdaNuevo/$',                login_required_view(MdaNuevo.as_view()), name='mda_new'),
    url(r'^MdaConsulta/(?P<pk>\d+)/$', login_required_view(MdaView.as_view()),  name='mda_view'),
    url(r'^MdaEdita/(?P<pk>\d+)/$',    login_required_view(MdaEdita.as_view()), name='mda_edit'),
    url(r'^MdaElimina/(?P<pk>\d+)/$',  login_required_view(MdaDelet.as_view()), name='mda_delet'),

    url(r'^CjrPanel',                  login_required_view(CjrLista.as_view()), name='cjr_panel'),
    url(r'^CjrNuevo/$',                login_required_view(CjrNuevo.as_view()), name='cjr_new'),
    url(r'^CjrConsulta/(?P<pk>\d+)/$', login_required_view(CjrView.as_view()),  name='cjr_view'),
    url(r'^CjrEdita/(?P<pk>\d+)/$',    login_required_view(CjrEdita.as_view()), name='cjr_edit'),
    url(r'^CjrElimina/(?P<pk>\d+)/$',  login_required_view(CjrDelet.as_view()), name='cjr_delet'),

    url(r'^CjaPanel',                  login_required_view(CjaLista.as_view()), name='cja_panel'),
    url(r'^CjaNuevo/$',                login_required_view(CjaNuevo.as_view()), name='cja_new'),
    url(r'^CjaConsulta/(?P<pk>\d+)/$', login_required_view(CjaView.as_view()),  name='cja_view'),
    url(r'^CjaEdita/(?P<pk>\d+)/$',    login_required_view(CjaEdita.as_view()), name='cja_edit'),
    url(r'^CjaElimina/(?P<pk>\d+)/$',  login_required_view(CjaDelet.as_view()), name='cja_delet'),

    url(r'^McjPanel',                  login_required_view(McjLista.as_view()), name='mcj_panel'),
    url(r'^McjNuevo/$',                login_required_view(McjNuevo.as_view()), name='mcj_new'),
    url(r'^McjConsulta/(?P<pk>\d+)/$', login_required_view(McjView.as_view()),  name='mcj_view'),
    url(r'^McjEdita/(?P<pk>\d+)/$',    login_required_view(McjEdita.as_view()), name='mcj_edit'),
    url(r'^McjElimina/(?P<pk>\d+)/$',  login_required_view(McjDelet.as_view()), name='mcj_delet'),
]

#if settings.DEBUG:
#	urlpatterns += [
#		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}
#			),
#	]
