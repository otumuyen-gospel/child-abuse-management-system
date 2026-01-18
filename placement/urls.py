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
    path('views/', PlacementList.as_view(), name='placement-list'),
    path('create/', CreatePlacement.as_view(), name='placement-create'),
    path('delete/<int:id>/', DeletePlacement.as_view(), name='placement-delete'),
    path('update/<int:id>/', UpdatePlacement.as_view(), name='placement-update'),
]
