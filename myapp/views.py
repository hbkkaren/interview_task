from django.shortcuts import render,get_object_or_404,redirect
from .models import Admin,Product,Orderplace

# Create your views here.


def index(request):
    if request.method =="POST":
        
    
        admin=Admin.objects.create(
            fullName = request.POST['fullName'],
            mobile = request.POST['mobile'],
            email = request.POST['email'],
        )
        product=Product.objects.create(
            productCompany = request.POST['productCompany']
        )
        Orderplace.objects.create(
            address = request.POST['address'],
            admin=admin,
            product=product
        )

        admin = Admin.objects.all()
        product = Product.objects.all()
        orderplace = Orderplace.objects.select_related('admin','product').all()

        return render(request,'order.html',{'orderplace':orderplace})
    else:
        return render(request,'index.html')



def clear(request):
    return render(request,'index.html')


def delete_order(request, pk):
    order_instance = Orderplace.objects.get(pk = pk)
    print(order_instance)
    order_instance.delete()
    return render(request,'order.html')  # Replace 'order_list' with the name of your list view

    






