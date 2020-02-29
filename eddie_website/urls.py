
from django.conf.urls import url, include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^$', views.homepage, name="homepage"),
    url(r'^contact/$', views.contactpage, name="contactpage"),
    url(r'^games/$', views.gamespage, name="gamespage"),
    url(r'^mental_game/$', views.mental_game, name="mental_game"),
    url(r'^music/$', views.musicpage, name="musicpage"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)