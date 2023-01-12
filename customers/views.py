from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


from .forms import CustomerForm


from .models import Customer


class CustomerView(generic.ListView):
    template_name = 'customers/home.html'
    context_object_name = 'latest_customer_list'
    queryset = Customer.objects.all()

    # def get_queryset(self):
    #     """
    #     Return the last five published questions (not including those set to be
    #     published in the future).
    #     """
    #     return Customer.objects.all()

# def home(request):
#     return render(request, 'customers/home.html')



def new_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():

            customer = form.save(commit=False)
            customer.save()
            return redirect('customers:customer_list')
    else:
        form = CustomerForm()
        
    context = { 'form': form }
    return render(request, 'customers/new.html', {'form': form})