from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import BeneficiaryForm, AddressForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login



from .models import Beneficiary

# Create your views here.
def index(request):
    return HttpResponse("hello world")

class BeneficiaryRegistration(View):
    template_name = 'create_beneficiary.html'

    def get(self, request):
        beneficiary_form = BeneficiaryForm()
        return render(request, self.template_name, {'beneficiary_form': beneficiary_form})

    def post(self, request):
        beneficiary_form = BeneficiaryForm(request.POST)

        if beneficiary_form.is_valid():
            beneficiary = beneficiary_form.save()
            # Redirect to the success page
            return redirect('Beneficiary:success')

        # If the form is not valid, re-render the registration page
        return render(request, self.template_name, {'beneficiary_form': beneficiary_form})


class AddAddress(View):
    template_name = 'add_address.html'

    def get(self, request):
        return render(request, self.template_name, {'address_form': AddressForm()})

    def post(self, request):
        address_form = AddressForm(request.POST)

        if address_form.is_valid():
            address_form.save()
            # Redirect to the 'create_beneficiary' URL after adding an address
            return redirect('Beneficiary:reg')

        return render(request, self.template_name, {'address_form': address_form})


def login_beneficiary(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the beneficiary page or any other page you want
            return redirect('Beneficiary:beneficiary_page')
        else:
            # Credentials are invalid, display an error message
            error_message = "Invalid username or password."

    return render(request, 'login_beneficiary.html', locals())
class BeneficiaryPageView(View):
    template_name = 'Beneficiary page.html'

    def get(self, request):
        return render(request, self.template_name)

