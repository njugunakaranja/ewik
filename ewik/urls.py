from django.contrib import admin  # Optional: only needed if using default admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages import views
from pages.admin_dashboard import admin_site  # Your custom EWIK admin site

urlpatterns = [
    # Custom branded admin site
    path('admin/', admin_site.urls),

    # Homepage
    path('', views.home, name='home'),

    # Dynamic page routing via slug
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
