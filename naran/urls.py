from django.contrib import admin
#importing path, include
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    #including urls of base
    path('', include('base.urls')),
]
