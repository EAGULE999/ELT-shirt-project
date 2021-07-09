from shop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_images, name='main_images'),
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:subcategory_slug>/', views.subcategory_list, name='subcategory_list'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
