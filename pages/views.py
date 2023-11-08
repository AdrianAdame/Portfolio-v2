from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect

from pages.forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "pages/about_me.html")

def contact(request):

    form = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Send email

            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email_from = form.cleaned_data['email']

            html = render_to_string("pages/email.html", request.POST)

            send_mail(
                "Message from " + name,     #Subject
                message,   # Email message/Content
                email_from, # Author
                [                  #
                    'adrian.adame@uabc.edu.mx'
                ],html_message = html
            )

            return redirect('home')

    else:
        # Send the html   

        form = ContactForm()
        
    return render(request, "pages/contact.html", {'form' : form})