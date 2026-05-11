from django.contrib import admin
from django.urls import path, include
from webapp.views import welcome, product, contact, register, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'), # /!\ CARE register isn't in the default django package

    path('', welcome, name='welcome'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
    path('accounts/profile/', profile, name='profile'),
    
]