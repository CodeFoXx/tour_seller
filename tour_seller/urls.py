"""tour_seller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tours/', include('tours.urls')),
    url(r'^touroperators/', include('touroperators.urls')),
    url(r'^places/', include('places.urls')),
    url(r'^consumers/', include('consumers.urls')),
    url(r'^airlines/', include('airlines.urls')),
    url(r'^$', views.index),
    url(r'^index', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^logon', views.logon, name='logon'),
    url(r'^reg/', include('logsys.urls')),
    url(r'^tour_seller/', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

