from django.conf.urls import include, url
from api.views import *
# Para la autentificacion de usuario 

from . import views as local_view
from rest_framework.authtoken import views as rest_framework_views


urlpatterns=[
	url(r'^explorer/$',explorer_list, name='explorer_list'),
	url(r'^explorer/(?P<pk>d+/$)', detalle, name='detalles'),
	url(r'^propiedad/$',propiedad_list, name= 'propiedad_list'),
	url(r'^propiedad/(?P<pk>\d+)/$',operacionPropiedad, name='operacionPropiedad'),
	url(r'^user/$',user_list, name= 'user_list'),
	url(r'^imagen/$',imageApi, name='imagen'),
# Session Login
    # url(r'^login/$', local_views.get_auth_token, name='login'),
    # url(r'^logout/$', local_views.logout_user, name='logout'),
    # url(r'^auth/$', local_views.login_form, name='login_form'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
] 