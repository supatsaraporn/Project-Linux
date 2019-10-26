from django.contrib import admin
from django.urls import path
from myapp import views as myappviews

urlpatterns = [
    path('', myappviews.index),
    path('services', myappviews.services),
    path('admin/', admin.site.urls),
]
