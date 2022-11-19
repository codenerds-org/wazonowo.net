from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings



from . import views
from .views import CreateCheckoutSessionView


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('item/<item_id>/', views.ItemDetails.as_view(), name='item_details'),
    path('config/', views.stripe_config),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]