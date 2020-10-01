"""djangoblog URL Configuration

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
from djangoblog.views import MyView, indexView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns;
from django.conf.urls.static import static
from django.conf import settings
# from articles import views as article_views
from articles.views import articlesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',  MyView.as_view(), name='about'),
    path('articles/',   include('articles.urls')),
    path('accounts/',   include('accounts.urls')),
    path('', articlesView.as_view(), name='index'),
]

urlpatterns += staticfiles_urlpatterns();
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)