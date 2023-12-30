from django.shortcuts import render, redirect
from .models import customers


# Create your views here.
def index(request):
    data = customers.objects.all()
    print(data)
    return render(request, "index.html", {"data": data})


def about_customer(request):
    return render(request, "about_customer.html")


def add_customer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        print(name, email, phone_number, address)
        query = customers(name=name,
                          email=email,
                          phone_number=phone_number,
                          address=address
                          )
        query.save()
        return redirect("/")
    return render(request, "index.html")


def updateCustomer(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']

        edit = customers.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.phone_number = phone_number
        edit.address = address
        edit.save()
        return redirect("/")

    d = customers.objects.get(id=id)
    return render(request, "update_customer.html", {"d": d})


def deleteCustomer(request, id):
    d = customers.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html", {"d": d})




