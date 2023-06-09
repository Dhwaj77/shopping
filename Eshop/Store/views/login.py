from django.shortcuts import render, redirect
from django.http import HttpResponse
from Store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session["customer"] = customer.id
                return redirect('homepage')

            else:
                error_msg = "Email or password invalid..!"
        else:
            error_msg = "Email or password invalid..!"

        # print(customer)
        return render(request, 'login.html', {'error': error_msg})

def logout(request):
    request.session.clear()
    return redirect('login')

                
