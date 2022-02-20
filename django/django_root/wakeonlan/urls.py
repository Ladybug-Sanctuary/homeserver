from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='wol-home'),
    path('wake/', views.wake, name='wol-wake'),
]
