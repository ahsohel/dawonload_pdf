from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('pdf_create', views.pdf_create, name='pdf_create'),

    path('new', views.new, name='new'),
    path('dashboard_customer_order_edit_Generate_Invoice', views.dashboard_customer_order_edit_Generate_Invoice, name='dashboard_customer_order_edit_Generate_Invoice'),

]