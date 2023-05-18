from django.contrib import admin
from django.urls import path
from .views import home,register,login_user,logout_user
from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
    
    path('blog/',views.PostList.as_view(), name='post_detail'),
    path('blog/',views.PostList.as_view(), name='post_detail'),
  
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
