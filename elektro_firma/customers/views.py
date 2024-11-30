from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Customer

@method_decorator(login_required, name='dispatch')
class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['name', 'address']
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('home')  # Redirect po úspěšném uložení
