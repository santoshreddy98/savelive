from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import home

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'',include('accounts.urls')),
    url(r'^$',home),
]
