from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
from .views import login_beneficiary
from .views import BeneficiaryPageView


app_name = 'Beneficiary'

urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.BeneficiaryRegistration.as_view(), name='reg'),
    path('login/', login_beneficiary, name='log'),
    path('add_address/', views.AddAddress.as_view(), name='add_address'),
    path('success/', TemplateView.as_view(template_name='success_page.html'), name='success'),
    path('beneficiary_page/', BeneficiaryPageView.as_view(), name='beneficiary_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
