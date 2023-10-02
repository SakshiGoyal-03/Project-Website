from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name="login"),
    path('home/', views.home, name="home"),
    path('logout/', views.dologout, name="dologout"),
    path('help/' , views.help , name="help"),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contactus.urls')),
    path('services/', include('services.urls')),
    
    
]

