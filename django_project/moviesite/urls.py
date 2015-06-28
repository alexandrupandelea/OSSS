from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'moviesite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('movierater.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
#url(r'^$', views.post_list)