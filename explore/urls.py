"""explore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import index
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index.front,name='front'),
    path('reg/',index.reg,name='reg'),
    path('login/',index.log_in,name='login'),
    path('home/',index.home,name='home'),
    path('main/',index.main_page,name='main_page'),
    path('profile_/',index.profile_,name='profile'),
    path('ask/',index.asked,name='ask'),
    path('logout/',index.logoutuser,name='logout_user'),
    path('explore/',index.explore,name='explore_ques'),
    path('personal/',index.personal,name='personal'),
    path('update/',index.update,name='update'),
    path('update_age/',index.update_age,name='update_age'),
    path('update_department/',index.update_department,name='update_department'),
    path('update_gender/',index.update_gender,name='update_gender'),
    path('update_address/',index.update_address,name='update_address'),
    path('update_email/',index.update_email,name='update_email'),
    path('update_bio/',index.update_bio,name='update_bio'),
    path('update_dp/',index.update_dp,name='update_dp'),
    path('update_workplace/',index.update_workplace,name='update_workplace'),
    path('admin/',admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)