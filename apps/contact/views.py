from django.shortcuts import render, redirect
from apps.contact.models import Contact


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )

        return redirect('contact')
    
    return render(request, 'contact.html')
