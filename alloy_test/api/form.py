from django import forms
from .models import SignupForm

class SignupFormForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput())
	last_name =  forms.CharField(widget=forms.TextInput())
	address_1 =  forms.CharField(widget=forms.TextInput())
	address_2 =  forms.CharField(widget=forms.TextInput(), required=False)
	city =  forms.CharField(widget=forms.TextInput())
	state =  forms.CharField(widget=forms.TextInput())
	zip_code =  forms.CharField(widget=forms.TextInput())
	country =  forms.CharField(widget=forms.TextInput())
	ssn =  forms.CharField(widget=forms.TextInput())
	email_address = forms.CharField(widget=forms.TextInput())
	phone_number = forms.CharField(widget=forms.TextInput())
	dob =  forms.CharField(widget=forms.TextInput())

	class Meta:
		model = SignupForm
		fields = [
			"first_name",
			"last_name",
			"address_1",
			"address_2",
			"city",
			"state",
			"zip_code",
			"country",
			"ssn",
			"email_address",
			"phone_number",
			"dob",
		]