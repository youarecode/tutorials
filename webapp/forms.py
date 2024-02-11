"""
A form is an elegant way for writing html forms.

my_form = CustomForm({'field':'value'})

print(my_form) as table by default
print(my_form.as_p()) as paragraph
print(my_form.as_ul()) as unordered list

my_form.is_valid() #true 

my_form.cleaned_data # which properties were valid
"""

from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()



