from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter your First Name'})
		self.fields['last_name'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter your Last Name'})
		self.fields['username'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter your Username'})
		self.fields['email'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter your Email'})
		self.fields['password1'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter your Password'})
		self.fields['password2'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Confirm your Password'})

	first_name = forms.CharField(max_length=150)
	last_name = forms.CharField(max_length=150)
	username = forms.CharField(max_length=150)
	email = forms.EmailField(max_length=150)
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter your Username'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter your Password'})
        
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'



	
