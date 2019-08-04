from django import forms


class ContactForm(forms.Form):
    your_email = forms.EmailField(required=False)
    message = forms.CharField(required=True, widget=forms.Textarea)
