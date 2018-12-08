from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # send_mail(
        #     'Property Listing Enquiry',
        #     'There has been enquiry for ' + listing + '. Sigin In into the admin pannel for more.',
        #     'anantarnav007@gmail.com',
        #     [realtor_email, 'anantarnav007@gmail.com'],
        #     fail_silently=False
        # )


        # Check if user has made an inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)
            if has_contacted:
                messages.error(request, 'You have already made the inquiry for this listing')
                return redirect('/listings/'+listing_id)
        
        contact = Contact(listing = listing ,listing_id = listing_id , name =  name , email = email , phone = phone , messsage = message, user_id = user_id)

        contact.save()


        messages.success(request, 'Your request has been successfully submitted')
        return redirect('/listings/'+listing_id)
