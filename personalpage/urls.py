from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emilabrahamdotcom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'personalpage.views.home', name='home'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^booklist/', include('booklist.urls', namespace='booklist')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^google9ac1f1994e374c06.html',
      TemplateView.as_view(template_name='google9ac1f1994e374c06.html')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
