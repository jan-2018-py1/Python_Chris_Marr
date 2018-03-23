from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.index),
    url(r'^users/(?P<user_id>\d+)$', views.show_user),
    url(r'^users/new_user$', views.new_user),
    url(r'^users/create_user$', views.create_user),
    url(r'^users/(?P<user_id>\d+)/edit_user$', views.edit_user),
    url(r'^users/(?P<user_id>\d+)/update_user$', views.update_user),
    url(r'^users/(?P<user_id>\d+)/destroy_user$', views.destroy_user)
]