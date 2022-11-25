from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addCustomer/', views.addCustomer, name='addCustomer'),
    path('addCustomer/addRecord/', views.addRecord, name='addRecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('updateCustomer/<int:id>', views.updateCustomer, name='updateCustomer'),
    path('updateCustomer/updateCustomerRecord/<int:id>', views.updateCustomerRecord, name='updateCustomerRecord')
]