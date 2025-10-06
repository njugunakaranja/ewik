from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # <-- NEW IMPORT

urlpatterns = [
    # Django Admin Site
    path('admin/', admin.site.urls),
    
    # Include the pages application's URLs at the site root ('').
    # This will handle the home page and future dynamic pages.
    path('', include('pages.urls')), 
]

# IMPORTANT: ONLY add this during development (when DEBUG=True) 
# to serve user-uploaded media files (images, documents).
if settings.DEBUG: # <-- NEW BLOCK
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
