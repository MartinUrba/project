from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, project_detail, user_list, home, about
from .views import project_detail
from .views import *

urlpatterns = [
    # Hlavní stránky
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('users/', user_list, name='user_list'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),


    # Projekty
    path('projects/', ProjectListView.as_view(), name='project-list'),  # Seznam projektů
    path('project/<int:pk>/', project_detail, name='project-detail'),  # Detail projektu
    path('projects/new/', ProjectCreateView.as_view(), name='project-create'),  # Přidání projektu
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project-edit'),  # Úprava projektu
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),  # Smazání projektu

    # Autentizace
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', UserRegisterView.as_view(), name='register'),

    # Zahrnutí výchozích cest pro autentizaci Django
    path('accounts/', include('django.contrib.auth.urls')),  # Zahrnutí výchozích URL pro autentizaci
]
