"""vbtournaments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Admin pages
    url(r'^admin/', include(admin.site.urls)),

    # Basis pages
    url(r'^', include('core.urls', namespace='core')),

    # Users pages
    url(r'^users/', include('accounts.urls', namespace='accounts')),

    # Login / logout
    url(r'^login$', 'accounts.views.login_user', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),

    # Register pages
    url(r'^register$', 'accounts.views.register', name='register'),
    url(r'^activation/(?P<activation_key>.+)$', 'accounts.views.activation', name='activation'),
    url(r'^new-activation-link/(?P<username>\d+)/$', 'accounts.views.new_activation_link', name='new_activation_link'),
]
