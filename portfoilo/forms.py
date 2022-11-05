from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name'}), error_messages={
        'required': 'Your name must not be empty!',
        'max_length': 'Please enter a shorter name, Maximum is 50 characters!'
    })

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), error_messages={
        'required': 'The Email Field must not be empty!',
    })
    # service_needed = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'This Should Be A Brief Details On Why You Contact Me'}), error_messages={
        'required': 'The Message Field Must Not Be Empty!',
    })
