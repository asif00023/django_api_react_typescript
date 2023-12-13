
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from dataprocessor import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('apis.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # ref: https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development
