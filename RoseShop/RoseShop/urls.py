from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'shop.views.page_not_found'
handler500 = 'shop.views.general_error_view'
handler403 = 'shop.views.permission_denied_view'
handler400 = 'shop.views.bad_request_view'

urlpatterns = [
    path('', include('shop.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
