from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta

from paddleusers.models import PaddleUser, Position


class UserRegisterForm(forms.ModelForm):
	error_messages = {
		'password_mismatch': "The two password fields didn't match.",
		'required': "This field is required.",
		'name_error': "Name can only contain letters.",
	}
	password1 = forms.CharField(label="Password",
		widget=forms.PasswordInput)
	password2 = forms.CharField(label="Password confirmation",
		widget=forms.PasswordInput,
		help_text="Enter the same password as above, for verification.")

	profile_picture = forms.ImageField(label="Profile picture",
		widget=forms.ClearableFileInput, required=False)


	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email")

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2

	def clean_first_name(self):
		firstname = self.cleaned_data.get("first_name")
		if not firstname:
			raise forms.ValidationError(
				self.error_messages['required'],
				code='invalid',
			)

		if not firstname.isalpha():
			raise forms.ValidationError(
				self.error_messages['name_error'],
				code='invalid',
			)
		return firstname

	def clean_last_name(self):
		lastname = self.cleaned_data.get("last_name")
		if not lastname:
			raise forms.ValidationError(
				self.error_messages['required'],
				code='invalid',
			)

		if not lastname.isalpha():
			raise forms.ValidationError(
				self.error_messages['name_error'],
				code='invalid',
			)
		return lastname

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])

		if commit:
			user.save()
		return user

class UserUpdateForm(forms.ModelForm):
	error_messages = {
		'required': "This field is required.",
		'name_error': "Name can only contain letters.",
	}

	class Meta:
		model = User
		fields = ("username", "email")


class UserUpdateForm(UpdateView):
	template_name = "profile.html"
	model = User
	form_class = UserUpdateForm
	success_url = "/"

class RegisterView(FormView):
	template_name = 'registration.html'
	form_class = UserRegisterForm

	success_url = "/"

	def form_valid(self, form):
		new_user = form.save()
		paddleuser = PaddleUser.create(profile_pic=form.cleaned_data["profile_picture"], user= new_user, paid_until=(datetime.now()+timedelta(days=7)))
		paddleuser.save()
		return super(RegisterView, self).form_valid(form)


class BoardView(ListView):
	template_name = 'board_page.html'
	queryset=Position.objects.all()

	def get_context_data(self, **kwargs):
		context = super(BoardView, self).get_context_data(**kwargs)
		context['board_positions'] = Position.objects.all().order_by('priority')
		return context