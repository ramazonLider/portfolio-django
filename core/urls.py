from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from app.api.views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'parts', PartViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/v3/', include(router.urls))
] 

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)
 urlpatterns += static(settings.STATIC_URL,
 document_root=settings.STATIC_ROOT)