from django.conf.urls import url,include
from .views import view_meds,view_list,search,profile,register,addmedicine,delete_med,update
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'home/$',view_meds,name='home'),
    url(r'list/$',view_list,name='list'),
    url(r'result/$',search,name='result'),
    url(r'login/$',login,{'template_name': 'accounts/login.html'},name='login'),
    url(r'logout/$',logout, {'template_name': 'accounts/home.html'},name='logout'),
    url(r'profile/$',profile,name='profile'),
    url(r'register/$',register,name='register'),
    url(r'profile/add/$',addmedicine,name='add'),
    url(r'profile/(?P<pk>\d+)/update/$',update,name='update'),
    url(r'profile/(?P<pk>\d+)/delete/$',delete_med,name='delete'),
]
