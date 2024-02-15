from django.urls import path
from users import views as user_views
from django.contrib.auth import views as authenticatios_views
from django.conf import settings
from django.conf.urls.static import static
app_name='users'
urlpatterns = [
    path('register/',user_views.register,name='register'),
    path('login/',authenticatios_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authenticatios_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profilepage,name='profile'),
    # path('login/',user_views.login,name='login'),
    # path('logout/',user_views.logout,name='logout'),
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
