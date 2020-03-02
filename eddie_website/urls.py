
from django.conf.urls import url, include
from django.contrib import admin
from .import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls.static import static
from django.conf import settings
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from products.views import all_products
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^$', views.homepage, name="homepage"),
    url(r'^contact/$', views.contactpage, name="contactpage"),
    url(r'^games/$', views.gamespage, name="gamespage"),
    url(r'^mental_game/$', views.mental_game, name="mental_game"),
    url(r'^music/$', views.musicpage, name="musicpage"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
