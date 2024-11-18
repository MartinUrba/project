from .forms import UserRegisterForm  # Tento import musíte přidat
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project
from .forms import ProjectForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponseNotAllowed
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'address', 'assigned_to']
    template_name = 'projects/project_form.html'
    success_url = '/'

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = '/'

class CustomLogoutView(View):
    def get(self, request):
        logout(request)  # Odhlásí uživatele
        return redirect('home')  # Přesměrování po odhlášení

    def get(self, request):
        return HttpResponseNotAllowed('GET method not allowed')

class UserRegisterView(FormView):
    template_name = 'registration/register.html'  # Templat pro zobrazení formuláře
    form_class = UserRegisterForm  # Nastavení formuláře pro registraci
    success_url = '/'  # Přesměrování po úspěšné registraci

    def form_valid(self, form):
        form.save()  # Uložíme nového uživatele
        return super().form_valid(form)

@login_required  # Tento dekorátor zajistí, že tuto stránku mohou vidět pouze přihlášení uživatelé
def user_list(request):
    users = User.objects.all()  # Získání všech uživatelů
    return render(request, 'user_list.html', {'users': users})