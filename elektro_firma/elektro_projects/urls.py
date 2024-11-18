from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views
from django.urls import include
from .views import UserRegisterView
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLogoutView

urlpatterns = [

    path('user-list/', views.user_list, name='user-list'),path('', home, name="home"),
    path('about/', about, name="about"),
    path('project/', views.ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', views.ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project-edit'),
    path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', include('django.contrib.auth.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Přesměrování po odhlášení
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]