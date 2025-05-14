from django.contrib import admin
from django.urls import path
from plants import views  # Make sure this import is correct
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # This now points to an existing view
    path('plants/', views.plant_list, name='plant_list'),
    path('suggest/', views.suggest_plants, name='suggest_plants'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)