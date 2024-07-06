from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
app_name = "projects"
urlpatterns = [
    path('', views.projects, name='all'),
    path('<uuid:pk>', views.project, name='get'),
    path('create/', views.create_project, name='create'),
    path('<uuid:pk>/edit/', views.edit_project, name='edit'),
    path('<uuid:pk>/delete/', views.delete_project, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)