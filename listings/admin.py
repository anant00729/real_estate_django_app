from django.contrib import admin

from .models import Listings

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price' )    

admin.site.register(Listings, ListingAdmin)  
