from .models import Contact
from django import forms
from django.core.validators import RegexValidator

alpha = RegexValidator(r"^[A-zÀ-ž\s']*$", 'Are you X Æ A-12 ? Numerical characters are not allowed')
alphanumeric = RegexValidator(r"^['0-9a-zA-Z]*$", 'Sorry, only alphanumerical characters allowed')


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        validators=[alpha],
        error_messages={'required': 'Nothing is not a valid name unfortunately 😕 Enter a name to make the machine happy.'},
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "oninvalid": "this.setCustomValidity('Enter a valid name.')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0 bg-trans",
                "pattern": "([A-zÀ-ž\s']){2,}"
            }
        )
    )

    email = forms.EmailField(
        label='',
        error_messages={'required': 'Enter a valid email address.'},
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "placeholder": "Mail",
                "oninvalid": "this.setCustomValidity('Enter a valid email address.')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0 bg-trans"
            }
        )
    )

    message = forms.CharField(
        label='',
        error_messages={'required': 'Your message seems quite empty, Fill the void with something nice 😉'},
        widget=forms.Textarea(
            attrs={
                "placeholder": "Message",
                "oninvalid": "this.setCustomValidity('Enter a valid message.')",
                "oninput": "setCustomValidity('')",
                "class": "form-control border-0 bg-trans",
                "rows": "5"
            }
        )
    )

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message'
        ]