from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import AdminStaffForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("hello world")


class AdminStaffRegistration(View):
    template_name = 'reg_admin.html'

    def get(self, request):
        AdminStaff_form = AdminStaffForm()
        return render(request, self.template_name, {'AdminStaff_form': AdminStaff_form})


class AdminStaffLogin(LoginView):
    template_name = 'login_admin.html'  # Specify the path to your login template
    success_url = reverse_lazy('AdminStaff:index')  # Redirect to a success page after login
