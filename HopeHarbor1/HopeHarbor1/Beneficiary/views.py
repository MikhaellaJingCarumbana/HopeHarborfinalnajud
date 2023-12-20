from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import BeneficiaryForm, AddressForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from .models import Beneficiary, Address
from .models import Goods_Tracker, Amount_Tracker
from django.db.models import Sum






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
            return redirect('Beneficiary:log')

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
        # Get the username and password from the form submission
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try to retrieve a Beneficiary with the provided username
        try:
            beneficiary = Beneficiary.objects.get(Username=username)
        except Beneficiary.DoesNotExist:
            beneficiary = None

        # Check if a Beneficiary was found and if the password matches
        if beneficiary and beneficiary.Password == password:
            # Authentication successful
            # Save the user ID in the session (for demonstration purposes; consider more secure options)
            request.session['user_id'] = beneficiary.UserID

            # Redirect to the beneficiary page or any other desired page
            return redirect('Beneficiary:beneficiary_page')
        else:
            # Authentication failed
            error_message = "Invalid username or password."

    # Render the login page with appropriate context
    return render(request, 'login_beneficiary.html', locals())
class BeneficiaryPageView(View):
    template_name = 'Beneficiary page.html'

    def get(self, request):
        return render(request, self.template_name)

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
            return redirect('Beneficiary:log')

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
        # Get the username and password from the form submission
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try to retrieve a Beneficiary with the provided username
        try:
            beneficiary = Beneficiary.objects.get(Username=username)
        except Beneficiary.DoesNotExist:
            beneficiary = None

        # Check if a Beneficiary was found and if the password matches
        if beneficiary and beneficiary.Password == password:
            # Authentication successful
            # Save the user ID in the session (for demonstration purposes; consider more secure options)
            request.session['user_id'] = beneficiary.UserID

            # Redirect to the beneficiary page or any other desired page
            return redirect('Beneficiary:beneficiary_page')
        else:
            # Authentication failed
            error_message = "Invalid username or password."

    # Render the login page with appropriate context
    return render(request, 'login_beneficiary.html', locals())
from django.shortcuts import get_object_or_404

class BeneficiaryPageView(View):
    template_name = 'Beneficiary page.html'

    def get(self, request):
        # Check if there is a logged-in user
        if 'user_id' in request.session:
            # Retrieve the user ID from the session
            user_id = request.session['user_id']

            # Retrieve the corresponding Beneficiary record
            beneficiary = Beneficiary.objects.get(UserID=user_id)

            # Retrieve goods tracker data
            goods_tracker_data = Goods_Tracker.objects.filter(beneficiary=beneficiary)

            amount_tracker_data = Amount_Tracker.objects.filter(beneficiary=beneficiary)

            # Calculate total amount using aggregate(Sum('Amount'))
            total_amount = amount_tracker_data.aggregate(Sum('Amount'))['Amount__sum'] or 0

            # Calculate total quantity using aggregate(Sum('Quantity'))
            total_quantity = goods_tracker_data.aggregate(Sum('Quantity'))['Quantity__sum'] or 0

            # Pass the beneficiary, goods tracker data, total amount, and total quantity to the template context
            context = {
                'beneficiary': beneficiary,
                'goods_tracker_data': goods_tracker_data,
                'amount_tracker_data': amount_tracker_data,
                'total_amount': total_amount,
                'total_quantity': total_quantity,  # Include the total_quantity variable
            }

            # Render the HTML page with the template context
            return render(request, self.template_name, context)

        # If no user is logged in, you may want to handle this case accordingly
        return render(request, 'login_beneficiary.html')

