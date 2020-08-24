from django.urls import include, path
# from django.
from django.conf import settings
from django.conf.urls.static import static, serve
from .views import (
    dashboard,
    register,
    complete_profile,
    vote,
    voted,
    Leader
)

app_name = 'contestant'

urlpatterns = [
    path('votefor/<str:user>/', vote, name='vote'),
    path('votedfor/<str:user>/', voted, name='voted'),
    path('accounts/', include("django.contrib.auth.urls"), name="accounts"),
    path('registration/', register, name='register'),
    path('registration/continue', complete_profile, name='continue'),
    path('dashboard/', dashboard, name='dashboard'),
    path('leaderboard/', Leader.as_view(), name='leaderboard'),
]
