"""webCV URL Configuration

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
from django.urls import path, include
from home import views as home
#from Post import views as Post
from CV import views as CV
from Posts import views as posts


urlpatterns = [
    path('admin/', admin.site.urls),
   # path('',home.index,name='home'),
   # path('post/',include('Post.urls')),
    path('',include('CV.urls')),
    path('posts', posts.home, name='home'),
    path('posts/',include('Posts.urls')),
    
]
