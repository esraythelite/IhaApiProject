from django.urls import re_path
from IhaApp import views

urlpatterns=[
    re_path(r'^user$', views.userLogin),
    re_path(r'^user/([0-9]+)$', views.userLogin),
    re_path(r'^iha$', views.ihaApi),
    re_path(r'^iha/([0-9]+)$', views.ihaApi)
]