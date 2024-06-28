from django.urls import path
from . import views


app_name = "projects"
urlpatterns = [
    path('', views.projects, name='all'),
    path('<uuid:pk>', views.project, name='get'),
    path('create/', views.create_project, name='create'),
    path('<uuid:pk>/edit/', views.edit_project, name='edit'),
    path('<uuid:pk>/delete/', views.delete_project, name='delete'),
]