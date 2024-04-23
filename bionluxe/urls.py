from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainApp.urls')),
    path('summernote/', include('django_summernote.urls')),
    path( "ads.txt",RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)