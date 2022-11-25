from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Customers
from django.urls import reverse
# Create your views here.

def index(request):
    customers = Customers.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        'myCustomers' : customers
    }
    return HttpResponse(template.render(context, request))

def addCustomer(request):
    template = loader.get_template("add-customer.html")
    return HttpResponse(template.render({}, request))

def addRecord(request):
    first = request.POST['firstname']
    last = request.POST['lastname']
    customer = Customers(firstname = first, lastname = last)
    customer.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    customer = Customers.objects.get(id=id)
    customer.delete()
    return HttpResponseRedirect(reverse('index'))

def updateCustomer(request, id):
    customer = Customers.objects.get(id=id)
    template = loader.get_template("update-customer.html")
    context = {
        'myCustomer': customer
    }
    return HttpResponse(template.render(context, request))

def updateCustomerRecord(request, id):
    first = request.POST['firstname']
    last = request.POST['lastname']
    customer = Customers.objects.get(id=id)
    customer.firstname = first
    customer.lastname = last
    customer.save()
    return HttpResponseRedirect(reverse("index"))