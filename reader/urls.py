from django.contrib import admin
from django.urls import path
from . import views
from .views import pdf1
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reader'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('pdf1/', views.pdf1, name='pdf1'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)