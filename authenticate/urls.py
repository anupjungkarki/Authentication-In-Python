from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.RegisterUser, name="register"),
    path('login', views.UserLogin, name="login"),
    path('content', views.content, name="content"),
    path('logout', views.LogoutUser, name="login"),
    path('profile', views.UserProfile, name="profile")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
