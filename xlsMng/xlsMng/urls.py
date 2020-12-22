from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api1 import views as v1
from rest_framework import routers

router = routers.DefaultRouter()

#router.register(r'upload',v1.FileView, basename='File')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file/',include('api1.urls')),
    path('',include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)