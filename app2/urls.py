from django.conf.urls import include, url
from django.contrib import admin
from  . import views

urlpatterns = [
	 url(r'^login/$',views.login ),
	 url(r'^files/$',views.get_files),
	 url(r'^listusers/$',views.list_users),
]
