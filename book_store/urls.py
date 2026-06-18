from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('books.urls')),
    path('', include('horse_tour.urls')),
    path('', include('myShop.urls')),
    path('', include('basket.urls')),
    path('', include('users.urls')),
    path('cineboard/', include('CineBoard.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)