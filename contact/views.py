from django.shortcuts import render
from .models import contactinfo, contactform

# Create your views here.
def contactus(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contactformdata = contactform(name=name, email=email, subject=subject, message=message)
        contactformdata.save()
        
        
    
    contactdata = contactinfo.objects.all()[0]
    
    context = {
        'contactinfo' : contactdata
    }
    
    return render(request, 'contact.html', context)