"""miniblog URL Configuration

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
from blog import views

# from django.views.static import serve
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.user_signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('addpost/', views.add_post, name='addpost'),
    path('updatepost/<int:id>', views.update_post, name='updatepost'),
    path('deletepost/<int:id>', views.delete_post, name='deletepost'),

    
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

