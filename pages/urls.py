from django.urls import path
from .views import home, page_detail

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', page_detail, name='page_detail'),
]
