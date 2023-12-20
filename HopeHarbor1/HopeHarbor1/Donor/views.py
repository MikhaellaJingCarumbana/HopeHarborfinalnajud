from datetime import date, timezone

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Donor
from .forms import Donor_Login_Form, Donor_Registration_Form
# Create your views here.

def index(request):
    return render(request, 'index.html')

class Cash(View):
    template='index.html'

    def get(self, request):
        uname = request.session['username']
        return render(request, self.template, {'Username': uname})

    def post(self, request):
        uname = request.session['username']
        request.session['username'] = uname
        return redirect('/cash')

class DiK(View):
    template='index.html'

    def get(self, request):
        uname = request.session['username']
        return render(request, self.template, {'Username': uname})

    def post(self, request):
        uname = request.session['username']
        request.session['username'] = uname
        return redirect('/goods')



def donor_entry_request(request):
    if request.method == "POST":
        form = Donor_Login_Form(request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('Username')
            Password = form.cleaned_data.get('Password')

            condition1 = Donor.objects.filter(Username=Username)
            condition2 = Donor.objects.filter(Password=Password)
            if condition1 and condition2:
                request.session['username'] = Username
                return HttpResponseRedirect('/donor/CashPage')
            elif condition1 and Password != condition2:
                raise ValidationError("Incorrect Password!")
            else:
                raise ValidationError("No user found!")
    else:
        form = Donor_Login_Form()

    return render(request, 'login.html', {'form' : form})

def registration(request):
    if request.method == 'POST':
        form = Donor_Registration_Form(request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('Username')

            condition1 = Donor.objects.filter(Username=Username)
            if condition1:
                raise ValidationError("User already exists!")
            else:
                form.save()
                return HttpResponse("Welcome Donor")
    else:
        form = Donor_Registration_Form()

    return render(request, 'registration.html', {'form':form})

class InsertGoods(View):
    template = 'DIKpage.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        quantity = request.POST['quantity']
        label = request.POST['label']
        perishable = 'perishable' in request.POST
        expiry = request.POST['expiry']
        cursor = connection.cursor()
        username = request.session['username']
        args = [perishable, expiry or None, label, username, quantity]
        cursor.callproc('InsertGoodsDonation', args)
        result = cursor.fetchall()
        cursor.close()
        print(result)
        msg = request.session['username']
        request.session['username'] = username
        return redirect('/goodstracker')



class displayGoodsTracker(View):
    template = 'DonationTracker.html'

    def get(self, request):
        donor_username = request.session['username']
        cursor = connection.cursor()
        cursor.callproc('DisplayGoodsTracker', [donor_username])
        results = cursor.fetchall()
        cursor.close()
        print(results)
        return render(request, self.template, {'results': results})

class InsertCashDonation(View):
    template = 'Cash.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        Amount = request.POST['amount']
        Date = date.today()
        Currency = request.POST['currency']
        AdminID = 1
        Username = request.session['username']

        cursor = connection.cursor()
        cursor.execute('SELECT UserID FROM donor_donor WHERE Username = %s', [Username])
        DonorID = cursor.fetchone()[0]
        cursor.close()

        cursor = connection.cursor()
        args = [Amount, Date, DonorID, Currency, AdminID]
        cursor.callproc('MakeDonation', args)
        result = cursor.fetchall()
        cursor.close()
        print(result)
        msg = request.session['username']
        request.session['username'] = Username
        return redirect('/donor/CashTracker')



class displayAmountTracker(View):
    template = 'Cash_Donations.html'

    def get(self, request):
        username = request.session['username']
        cursor = connection.cursor()
        cursor.callproc('DisplayCashTracker', [username])
        results = cursor.fetchall()
        cursor.close()
        return render(request, self.template, {'results': results})
