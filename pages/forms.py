from django.forms import (
    Form,
    CharField,
    EmailField,
    Textarea,
    TextInput
)

class ContactForm(Form):
    name = CharField(max_length = 225, widget = TextInput(attrs = {'placeholder': 'Name'}))
    email = EmailField(widget = TextInput(attrs = {'placeholder': 'Email'}))
    message = CharField(widget= Textarea(attrs = {'placeholder': 'Message'}))
