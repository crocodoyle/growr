from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from track import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    url(r'^(?P<kid_id>\d+)/$', views.display, name='display'),
    url(r'^(?P<kid_id>\d+)/measure/$', views.measure, name='measure'),
    url(r'update/', views.update, name='update')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^images/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
    
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))