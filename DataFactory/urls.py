"""DataFactory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from factory import views as fv
from user import views as uv
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('forcode/',ForCodeView.as_view(),name='forcode'),
    url(r'^index/$', fv.index),
    url(r'^file_upload/$', fv.file_upload),
    url(r'^table_basic/$', fv.table_basic),
    url(r'^table_complete/$', fv.table_cmplete),
    url(r'^chart_columnar/$', fv.chart_columnar),
    url(r'^data/$', fv.data),
    url(r'^chart_line/$', fv.chart_line),
    url(r'^chart_pie/$', fv.chart_pie),
    url(r'^chart_scatter/$', fv.chart_scatter),
    url(r'^get_data/$', fv.get_data),
    url(r'^clear_data/$', fv.clear_data),
    url(r'^typography/$', uv.typography),
    url(r'^login/$', uv.login),
    url(r'^page_recoverpw/$', uv.page_recoverpw),
    url(r'^change_pswd$', uv.change_pswd),
    url(r'^register/$', uv.register),
    url(r'^permission_assignment/$', uv.permission_assignment),
    url(r'^user_manage/$', uv.user_manage),
    url(r'^logout/$', uv.logout),
    url(r'^delete_user/$', uv.delete_user),
    url(r'^update_user/$', uv.update_user),
    url(r'^send_forcode/$', uv.send_forcode),
    url(r'^pie_data/$', fv.pie_data),

]
