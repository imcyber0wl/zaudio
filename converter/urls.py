from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views 

urlpatterns = [
    path('', views.home),
    path('checkfile/', views.check_file),
    path('download/',views.download_view),
    #path('admin/', admin.site.urls),
]
