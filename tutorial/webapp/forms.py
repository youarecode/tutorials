from django import forms

# A form is an elegant way for writing html forms.
class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

