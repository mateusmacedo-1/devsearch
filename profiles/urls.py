from django.urls import path
from . import views

app_name = "profiles"
urlpatterns = [
    path('', views.profiles, name='list'),
    path('<uuid:pk>', views.profile, name='get'),
]