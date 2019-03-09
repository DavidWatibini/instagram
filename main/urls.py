from django.conf.urls import url,include
from django.conf import settings
from . import views


urlpatterns = [
    # url(r'^$', views.insta_index),
    url(r'^home/$',views.home_index, name="homePage"),
    url(r'^$', views.signup),
    url(r'accounts/', include('django.contrib.auth.urls')),
]
