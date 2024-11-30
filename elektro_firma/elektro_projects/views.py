from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Project
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import ProjectForm
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'  # Šablona pro seznam projektů
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        customer_query = self.request.GET.get('customer')  # Hodnota z GET parametru
        assigned_to_query = self.request.GET.get('assigned_to')  # Hodnota z GET parametru

        # Filtrování podle zákazníka
        if customer_query:
            queryset = queryset.filter(customer__icontains=customer_query)

        # Filtrování podle přidělené osoby
        if assigned_to_query:
            queryset = queryset.filter(assigned_to__username__icontains=assigned_to_query)

        return queryset


from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'elektro_projects/project_detail.html', {'project': project})

# Vytvoření projektu
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')

# Úprava projektu

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list') # Přesměrování na seznam projektů

    def get_queryset(self):
        return self.model.objects.all()


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')


class UserRegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrace proběhla úspěšně!')
            return redirect('login')
        messages.error(request, 'Došlo k chybě při registraci.')
        return render(request, 'registration/register.html', {'form': form})

def user_list(request):
        users = User.objects.all()
        return render(request, 'registration/user_list.html', {'users': users})