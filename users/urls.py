from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
app_name = "users"
urlpatterns = [
    path('', views.users, name='all'),
]