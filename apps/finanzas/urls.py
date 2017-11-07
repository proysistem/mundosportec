from django.conf.urls import include, url
from .views import  CjaLista, CjaNuevo, CjaView, CjaEdita, CjaDelet, CjrLista, CjrNuevo, CjrView, CjrEdita, CjrDelet, McjLista, McjNuevo, McjView, McjEdita, McjDelet, MdaLista, MdaNuevo, MdaView, MdaEdita, MdaDelet

urlpatterns = [

    url(r'^MdaPanel',                  MdaLista.as_view(), name='mda_panel'),
    url(r'^MdaNuevo/$',                MdaNuevo.as_view(), name='mda_new'),
    url(r'^MdaConsulta/(?P<pk>\d+)/$', MdaView.as_view(),  name='mda_view'),
    url(r'^MdaEdita/(?P<pk>\d+)/$',    MdaEdita.as_view(), name='mda_edit'),
    url(r'^MdaElimina/(?P<pk>\d+)/$',  MdaDelet.as_view(), name='mda_delet'),

    url(r'^CjrPanel',                  CjrLista.as_view(), name='cjr_panel'),
    url(r'^CjrNuevo/$',                CjrNuevo.as_view(), name='cjr_new'),
    url(r'^CjrConsulta/(?P<pk>\d+)/$', CjrView.as_view(),  name='cjr_view'),
    url(r'^CjrEdita/(?P<pk>\d+)/$',    CjrEdita.as_view(), name='cjr_edit'),
    url(r'^CjrElimina/(?P<pk>\d+)/$',  CjrDelet.as_view(), name='cjr_delet'),

    url(r'^CjaPanel',                  CjaLista.as_view(), name='cja_panel'),
    url(r'^CjaNuevo/$',                CjaNuevo.as_view(), name='cja_new'),
    url(r'^CjaConsulta/(?P<pk>\d+)/$', CjaView.as_view(),  name='cja_view'),
    url(r'^CjaEdita/(?P<pk>\d+)/$',    CjaEdita.as_view(), name='cja_edit'),
    url(r'^CjaElimina/(?P<pk>\d+)/$',  CjaDelet.as_view(), name='cja_delet'),

    url(r'^McjPanel',                  McjLista.as_view(), name='mcj_panel'),
    url(r'^McjNuevo/$',                McjNuevo.as_view(), name='mcj_new'),
    url(r'^McjConsulta/(?P<pk>\d+)/$', McjView.as_view(),  name='mcj_view'),
    url(r'^McjEdita/(?P<pk>\d+)/$',    McjEdita.as_view(), name='mcj_edit'),
    url(r'^McjElimina/(?P<pk>\d+)/$',  McjDelet.as_view(), name='mcj_delet'),
]

#if settings.DEBUG:
#	urlpatterns += [
#		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}
#			),
#	]