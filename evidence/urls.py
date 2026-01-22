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

from django.urls import path
from .views import *
'''
 Each time a new faces is uploaded or an existing one is updated, admin should 
 remember to cache the face encodings again using the cache management endpoint.
'''
urlpatterns = [
    path('files/views/', EvidenceList.as_view(), name='evidence-list'),
    path('files/upload/', CreateEvidence.as_view(), name='create-evidence'),
    path('files/delete/<int:id>/', DeleteEvidence.as_view(), name='delete-evidence'),
    path('files/update/<int:id>/', UpdateEvidence.as_view(), name='evidence-update'),
    
]
