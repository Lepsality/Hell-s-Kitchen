from django.shortcuts import render, HttpResponseRedirect
from .models import Menu, Reservation, PizzaRestaurant
from .forms import ReservationForm


def menu(request):
    menu_items = Menu.objects.prefetch_related('prices__size')
    menu_data = []
    for item in menu_items:
        item_dict = {
            'id': item.id,
            'name': item.name,
            'picture': item.picture.url if item.picture else None,
            'description': item.description,
            'sizes': {}
        }
        for price in item.prices.all():
            item_dict['sizes'][price.size.name] = price.price
        menu_data.append(item_dict)
    return render(request, 'pizza/menu.html', {'menu_items': menu_data})


def get_reserv(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data
            new_reservation = Reservation(name=result['name'], phone=result['phone'], date=result['date'])
            new_reservation.save()
            return HttpResponseRedirect('/')
    else:
        form = ReservationForm()
    return render(request, 'pizza/Reservation.html', {'form': form})


def about_us(request):
    restaurant = PizzaRestaurant.objects.get(name="Hell's Kitchen")
    context = {'restaurant': restaurant}
    return render(request, 'pizza/about_us.html', context)