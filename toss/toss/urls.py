"""toss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from accounts.api.viewsets import AccountViewSet
from activities.api.viewsets import ActivityViewSet

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

api_router = routers.DefaultRouter()
api_router.register(r'accounts', AccountViewSet, base_name='accounts')
api_router.register(r'activities', ActivityViewSet, base_name='activities')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(api_router.urls)),
]
