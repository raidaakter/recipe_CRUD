"""
URL configuration for recipeManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from RecipeApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('add_recipe',add_recipe, name="add_recipe"),
    path('edit_recipe<str:id>/',edit_recipe, name="edit_recipe"),
    path('delete_recipe/<str:id>/',delete_recipe, name="delete_recipe"),
    path('view_recipe<str:id>/',view_recipe, name="view_recipe")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
