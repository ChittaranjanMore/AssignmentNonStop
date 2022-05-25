from multiprocessing import context
from django import views
from django.shortcuts import redirect, render
from .models import Product, User, Recommendation
from django.views import View
from django.core.paginator import Paginator
# Create your views here.

class AboutUsView(View):

    def get(self, request):
        return render(request,"about.html")


class UserView(View):

    def get(self, request):
        data = User.objects.all().values()  
        context = {"data":data}
        return render(request,"user.html",context)


class AddUserView(View):

    def get(self, request):
        return render(request,"add_user.html")

    def post(self, request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        user = User(name=name,age=age,address=address)
        user.save()
        
        data = User.objects.all().values()  
        context = {"data":data}
        return render(request,"user.html",context)


class AddProductView(View):

    def get(self, request):
        return render(request,"add_product.html")

    def post(self, request):
        shape = request.POST.get('shape')
        size = request.POST.get('size')
        location = request.POST.get('location')
        price = request.POST.get('price')
        product_data = Product(shape = shape, size = size, location = location, price = float(price))
        product_data.save()
        
        context = pagination(request)
        return render(request,"product.html",context)


class ProductView(View):

    def get(self, request):
        context = pagination(request)
        return render(request,"product.html",context)


class UserUpdateView(View):

    def get(self, request, id):
        data = User.objects.get(pk = id)
        context = {"data":data}
        return render(request, "user_update.html",context)

    def post(self, request, id):
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        user_data = User.objects.get(pk=id)
        
        user_data.name = name
        user_data.age = age
        user_data.address = address

        user_data.save()

        data = User.objects.all().values()
        context = {"data":data}
        return render(request,"user.html",context)


class ProductUpdateView(View):

    def get(self, request, id):
        data = Product.objects.get(pk = id)
        context = {"data":data}
        return render(request, "product_update.html",context)

    def post(self, request, id):
        shape = request.POST.get('shape')
        size = request.POST.get('size')
        location = request.POST.get('location')
        price = request.POST.get('price')
        product_data = Product.objects.get(pk=id)
        
        product_data.shape = shape
        product_data.size = size
        product_data.location = location
        product_data.price = float(price)

        product_data.save()

        context = pagination(request)
        return render(request,"product.html",context)


def pagination(request):
    data = Product.objects.all().values().order_by("-id")  
    page = request.GET.get('page', 50)
    paginator = Paginator(data, 50)
    users = paginator.page(page)
    context = {"page_number":users}
    return context