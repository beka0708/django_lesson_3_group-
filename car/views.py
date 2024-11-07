from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Car
from .forms import CarForm


# list-car
def car_list_view(request):
    car_objects = Car.objects.all()
    return render(request, 'car_list.html', {
        'car_objects': car_objects
    })


# id-car
def car_detail_view(request, id):
    car_detail = get_object_or_404(Car, id=id)
    return render(request, 'car_detail.html', {
        'car_detail': car_detail
    })


# create-car
def create_car_view(request):
    method = request.method
    if method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Машина успешно добавлена!</h2>")
    else:
        form = CarForm()
    return render(request, 'create_car.html', {
        "form": form
    })


# update-car
def update_car_view(request, id):
    car_object = get_object_or_404(Car, id=id)
    if request.method == "POST":
        form = CarForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Машина успешно обновлена</h2>")
    else:
        form = CarForm(instance=car_object)
        return render(request, 'update_car.html', {
            "form": form, "object": car_object
        })


# car-delete
def delete_car_view(request, id):
    car_object = get_object_or_404(Car, id=id)
    car_object.delete()
    return HttpResponse("<h2>Машина успешно удалена</h2>")
