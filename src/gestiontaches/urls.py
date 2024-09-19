"""
URL configuration for gestiontaches project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework import routers
from project.viewsets.project_viewset import ProjectViewSet
from project.viewsets.task_viewset import TaskViewSet
from team.viewsets.team_viewset import TeamViewSet
from team.viewsets.member_viewset import MemberViewSet
from project.viewsets.summons_viewset import SummonsViewSet
from history.views import Notification


router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'task', TaskViewSet)
router.register(r'team', TeamViewSet)
router.register(r'member', MemberViewSet)
router.register(r'summons', SummonsViewSet)
router.register(r'notifications', Notification)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
