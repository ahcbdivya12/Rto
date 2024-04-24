"""
URL configuration for real_rto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rto_web import views as rto_users

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('rto_office/', include('service.urls')),

    path('signup',rto_users.singup),  
    path('u_login',rto_users.user_login),    
    path('logout',rto_users.LogoutPage,name='logout'),
    path('forget',rto_users.forget,name='forget'),

    path('',rto_users.index ),
	path('category',rto_users.category),
	path('about',rto_users.about),
	path('contact',rto_users.contact),
	path('guid',rto_users.guid),
	path('l_form',rto_users.l_form),
    path('confirm',rto_users.confirm),
    path('appoinment',rto_users.appoinment),
    path('change_confirm',rto_users.change_confirm),
    path('print_from',rto_users.print_from),
    path('change_info', rto_users.change_info, name='change_info'),
    path('change_address', rto_users.change_address),
    path('mobile_number_change', rto_users.mobile_number_change),
    path('name_change', rto_users.name_change),
    path('prent_change', rto_users.prent_change),
    path('change_confirm_renewal', rto_users.change_confirm_renewal),
    path('renewal', rto_users.renewal),
    path('duplicate_form', rto_users.duplicate_form),
    path('rc_book', rto_users.rc_book),
    
    path('vehical_info',rto_users.vehical_info,name="vehical_info"),

    path('checkout', rto_users.create_checkout_session, name='checkout'),
    path('success', rto_users.success, name='success'),
    path('cancel', rto_users.cancel, name='cancel'),

    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
