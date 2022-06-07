
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', admin.site.urls),
    path(route='', view= views.home, name='home'),
    path(route='nosotros', view= views.nosotros, name='nosotros'),
]
 