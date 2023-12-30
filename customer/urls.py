from django.urls import path
from customer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_customer, name='about_customer'),
    path('add', views.add_customer, name='add_customer'),
    path('update/<id>', views.updateCustomer, name='updateCustomer'),
    path('delete/<id>', views.deleteCustomer, name='deleteCustomer'),

]
