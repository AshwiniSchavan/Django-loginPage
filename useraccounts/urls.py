from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

app_name = 'useraccounts'

urlpatterns = [
    url(r'^$',  views.home, name='home'),
    url(r'^login/$', auth_view.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_view.logout,name='logout'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]
