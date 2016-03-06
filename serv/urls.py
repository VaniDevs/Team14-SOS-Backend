from django.conf.urls import include, url
from rest_framework import routers
from django.contrib import admin
from app import views
admin.autodiscover()



# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

#router = routers.DefaultRouter()
#router.register(r'user', views.user_lookup)
#router.register(r'sos', views.SosViewSet)

urlpatterns = [
    url(r'^user/$', views.user_lookup),
    url(r'^user/(?P<pk>[-\w]+)$', views.user_detail),
    url(r'^sos/$', views.sos_lookup),
    url(r'^sos/(?P<pk>[-\w]+)$', views.sos_detail),
    url(r'^sos/(?P<pk>[-\w]+)/status/$', views.sos_status),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
