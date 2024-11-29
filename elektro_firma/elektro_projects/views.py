from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Project
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'  # Cesta k šabloně pro zobrazení seznamu projektů
    context_object_name = 'projects'


from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'elektro_projects/project_detail.html', {'project': project})

# Vytvoření projektu
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'address', 'customer', 'assigned_persons']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')  # Po úspěšném přidání přesměrování na seznam projektů

# Úprava projektu
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'address', 'customer', 'assigned_persons']
    template_name = 'projects/project_form.html'

    def get_queryset(self):
        # Umožní upravit pouze projekty, které patří přihlášenému uživateli
        return self.model.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        project = form.save(commit=False)
        project.owner = self.request.user  # Ujistíme se, že je vlastník správný
        project.save()
        return super().form_valid(form)

def user_list(request):
    users = User.objects.all()
    return render(request, 'registration/user_list.html', {'users': users})

# Smazání projektu s potvrzením
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')

    def get_queryset(self):
        # Umožní smazat pouze projekty, které patří přihlášenému uživateli
        return self.model.objects.filter(owner=self.request.user)

class UserRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})