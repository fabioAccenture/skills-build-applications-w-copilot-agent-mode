"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from octofit_tracker import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
        'teams': reverse('teams-list', request=request, format=format),
        'activities': reverse('activities-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workouts-list', request=request, format=format),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/users/', views.UserList.as_view(), name='users-list'),
    path('api/teams/', views.TeamList.as_view(), name='teams-list'),
    path('api/activities/', views.ActivityList.as_view(), name='activities-list'),
    path('api/leaderboard/', views.LeaderboardList.as_view(), name='leaderboard-list'),
    path('api/workouts/', views.WorkoutList.as_view(), name='workouts-list'),
]
