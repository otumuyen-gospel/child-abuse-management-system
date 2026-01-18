"""
URL configuration for backend project.

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

from typing import List
from django.urls import path
from .views import *
urlpatterns = [
    path('views/', ActionList.as_view(), name='action-list'),
    path('create/', CreateAction.as_view(), name='action-create'),
    path('delete/<int:id>/', DeleteAction.as_view(), name='action-delete'),
    path('update/<int:id>/', UpdateAction.as_view(), name='action-update'),
]
