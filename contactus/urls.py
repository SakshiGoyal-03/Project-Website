from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('' , views.contact, name="contact"),
]