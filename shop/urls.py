from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('', views.home, name='homepage'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('', include('shop.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="shop/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='shop/password/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset', views.password_reset_request, name='password_reset'),
]
