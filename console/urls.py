from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.console_home, name='console'),
    url(r'telemetry$', views.get_telemetry, name='telemetry'),
    url(r'api$', views.post_telemetry, name='api'),
    url(r'hooks$', views.hook_telemetry, name='hooks'),
]
