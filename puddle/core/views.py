from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import SignUpForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    contact_info = {
        'phone': ' +254740383489',
        'email': ' faithsang001@gmail.com',
        'location': ' Maasai Lodge road, Vanna House 5th floor'
    }
    return render(request, 'core/contact.html', {
        'contact_info': contact_info
    })

def about(request):
    con = {
        'company_description': 'This is an e-commerce website built by Kj a final year student at Multimedia university of kenya.The website enables a user to signup, login then be able to view the items available for purchase. Once  the user selects an item they are intrested in they can contact the seller to be able to purchase it. They can also put item they would like to sell and become the seller.'
    }
    return render(request, 'core/about.html', con)

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

