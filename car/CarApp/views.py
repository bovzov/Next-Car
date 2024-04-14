from django.shortcuts import render,redirect
from .models import Car,Brand
from .forms import ContactForm
from .models import Contact


def HomeView(request):
    car1 = Car.objects.all().order_by('id')[0]
    brands = Brand.objects.all()
    electric_cars = Car.objects.filter(engine='ELEKTR').order_by('id')[:5]
    cars_by_brand = Car.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            client = Contact.objects.create(
                name = form.cleaned_data['name'],
                phonenumber = form.cleaned_data['phonenumber']
            )
            client.save()

            return redirect('home')
    else:
        form = ContactForm()
    
    
    context = {
        'car1': car1,
        'brands': brands,
        'electric_cars': electric_cars,
        'cars_by_brand':  cars_by_brand,
        'form': form
        
    }
    
    return render(request, 'index.html',context)


