"""
URL configuration for apis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agency/', include('agency.urls'), name='agency'),
    path('role/', include('role.urls'), name='Roles'),
    path('permissions/', include('permissions.urls'), name='Permissions'),
    path("person/",include('person.urls'), name="Person"),
    path("contact/",include('contact.urls'), name="Contact"),
    path("user/",include('user.urls'), name="Users"),
    path("auth/",include('auth.urls'), name="Auth Pages"),
    path("message/",include('message.urls'), name="Message"),
    path("abuse_type/",include('abuse_type.urls'), name="Abuse Types"),
    path("action/",include('action.urls'), name="Actions"),
    path("allegation/",include('allegation.urls'), name="Allegations"),
    path("case/",include('case.urls'), name="Cases"),
    path("investigation/",include('investigation.urls'), name="Investigations"),
    path("perpetrators/",include('perpetrators.urls'), name="Perpetrators"),
    path("victims/",include('victims.urls'), name="Victims"),
    path("reporters/",include('reporters.urls'), name="Reporters"),
    path("reports/",include('reports.urls'), name="Reports"),
    path("placement/",include('placement.urls'), name="Placements"),
    path("screening/",include('screening.urls'), name="Screenings"),
    path("services/",include('services.urls'), name="Services"),
    path("worker/",include('worker.urls'), name="Workers"),
     path("evidence/",include('evidence.urls'), name="Evidence"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
