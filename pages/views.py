from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listings
from realtors.models import Realtor
from listings.choises import bedroom_choices,price_choices,state_choices

# Create your views here.
def index(request):
    
    listings = Listings.objects.order_by('-list_date').filter(is_published = True)[:3]

    context = {
        'listings' : listings,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'state_choices' : state_choices
    }


    return render(request, 'pages/index.html',context)


def about(request):
    # Only Realtors
    realtors = Realtor.objects.order_by('-hire_date')
    
    # all the mvp Realtors
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context  = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }

    return render(request, 'pages/about.html', context)    