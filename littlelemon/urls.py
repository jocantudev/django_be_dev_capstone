#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register(r'tables',views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
]