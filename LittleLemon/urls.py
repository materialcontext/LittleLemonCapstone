from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from LittleLemonAPI import views

# Create a router and register your viewset with it.
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='bookings')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('LittleLemonAPI.urls')),
   path('bookings/', include(router.urls)),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken')),
]
