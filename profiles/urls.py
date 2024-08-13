from django.urls import include, path
from . import views

app_name = "profiles"

skill_urlpatterns = [
    path("create/", views.create_skill, name="create-skill"),
    path("edit/<uuid:pk>", views.edit_skill, name="edit-skill"),
    path("delete/<uuid:pk>", views.delete_skill, name="delete-skill"),
]

personal_urlpatterns = [
    path('', views.personal_profile, name='personal'),
    path('skills/', include(skill_urlpatterns)),
    path('inbox/', views.inbox, name='inbox'),
]

urlpatterns = [
    path('', views.profiles, name='list'),
    path('<uuid:pk>/', views.profile, name='get'),
    path('personal/', include(personal_urlpatterns)),
    
]