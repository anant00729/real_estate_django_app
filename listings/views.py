from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .choises import bedroom_choices,price_choices,state_choices


from .models import Listings

def index(request):
  listings = Listings.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 3)

  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)


  context = {
    'listings' : paged_listings
  }
  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  
  listing = get_object_or_404(Listings, pk=listing_id)

  context = {
    'listing' : listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):

  query_set_listings = Listings.objects.order_by('-list_date')

  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      query_set_listings = query_set_listings.filter(description__icontains = keywords)

  if 'city' in request.GET:
    city = request.GET['city']      
    if city:
      query_set_listings = query_set_listings.filter(city__icontains = city)

  if 'state' in request.GET:
    state = request.GET['state']      
    if state:
      query_set_listings = query_set_listings.filter(state__icontains = state)      

  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']      
    if bedrooms:
      query_set_listings = query_set_listings.filter(bedrooms__icontains = bedrooms)      

  if 'price' in request.GET:
    price = request.GET['price']      
    if price:
      query_set_listings = query_set_listings.filter(price__lte = price)     

                     

  context = {
    'bedroom_choices' : bedroom_choices,
    'price_choices' : price_choices,
    'state_choices' : state_choices,
    'listings' : query_set_listings,
    'values' : request.GET
  }
  print(context)
  return render(request, 'listings/search.html',context)    



