from shop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_products, name='all_products'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
