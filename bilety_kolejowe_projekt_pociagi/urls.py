"""
URL configuration for bilety_kolejowe_projekt_pociagi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from Bilety_i_pociagi.views import index, SignUpView, search_trains
#? serializers
from Bilety_i_pociagi.views import CitySearchView, login_view, logout_view, user_status


urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name="logout"),
    path('admin/', admin.site.urls),
    #? serializers
    path('api/cities/', CitySearchView.as_view(), name='city-search'),
    path('api/search_trains/', search_trains, name='search_trains'),
    path('api/user/login', login_view, name='login'),
    path('api/user/logout', logout_view, name='logout'),
    path('api/user/status', user_status, name='user_status'),
]
