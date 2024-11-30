from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, project_detail, user_list, home, about
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Hlavní stránky
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('users/', user_list, name='user_list'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Projekty
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', project_detail, name='project-detail'),
    path('projects/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project-edit'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),

    # Admin panel
    path('admin/', admin.site.urls),  # Odkaz na admin panel

    # Zákazníci a osoby
    path('customers/', include('customers.urls')),
    path('people/', include('people.urls')),

    # Autentizace
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserRegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
