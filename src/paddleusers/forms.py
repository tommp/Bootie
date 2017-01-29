from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login

from paddleusers.models import PaddleUser
from captcha.fields import CaptchaField


class UserRegisterForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
        'required': "This field is required.",
        'name_error': "Name can only contain letters.",
    }

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification."
    )

    profile_picture = forms.ImageField(
        label="Profile picture",
        widget=forms.ClearableFileInput,
        required=False
    )

    captcha = CaptchaField(required=True)


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "captcha")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password1:
            forms.ValidationError(
                self.error_messages['required'],
                code='password_mismatch',
            )

        if not password2:
            forms.ValidationError(
                self.error_messages['required'],
                code='password_mismatch',
            )

        if (password1 != password2):
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

        if not firstname.replace(' ','').isalpha():
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

        if not lastname.replace(' ','').isalpha():
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

    captcha = CaptchaField(required=True)

    profile_picture = forms.ImageField(
        label="Profile picture",
        widget=forms.ClearableFileInput,
        required=False
    )

    delete_profile_pic = forms.BooleanField(label="Delete profile picture", required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "captcha", "profile_picture", "delete_profile_pic")


class UserUpdateForm(FormView):
    template_name = "profile.html"
    form_class = UserUpdateForm
    success_url = "/"

    def get_initial(self):
        paddleuser = PaddleUser.objects.get(user=self.request.user)
        initial = super(UserUpdateForm, self).get_initial()
        initial["first_name"] = paddleuser.user.first_name
        initial["last_name"] = paddleuser.user.last_name
        initial["email"] = paddleuser.user.email
        return initial

    def form_valid(self, form):
        paddleuser = PaddleUser.objects.get(user=self.request.user)
        update_user = paddleuser.user
        update_user.first_name = form.cleaned_data["first_name"]
        update_user.last_name = form.cleaned_data["last_name"]
        update_user.email = form.cleaned_data["email"]
        if form.cleaned_data["delete_profile_pic"]:
            paddleuser.profile_pic = ""
        elif form.cleaned_data["profile_picture"]:
            paddleuser.profile_pic = form.cleaned_data["profile_picture"]
        paddleuser.save()
        update_user.save()
        return super(UserUpdateForm, self).form_valid(form)


class RegisterView(FormView):
    template_name = 'registration.html'
    form_class = UserRegisterForm

    success_url = "/"

    def form_valid(self, form):
        new_user = form.save()

        paddleuser = PaddleUser.create(
            profile_pic=form.cleaned_data["profile_picture"],
            user=new_user,
            paid_until=(datetime.now()+timedelta(days=7))
        )

        paddleuser.save()

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"]
        )

        login(self.request, user)

        return super(RegisterView, self).form_valid(form)


class UserDeleteForm(forms.ModelForm):
    error_messages = {
        'required': "This field is required.",
    }

    captcha = CaptchaField(required=True)

    class Meta:
        model = User
        fields = ("captcha",)


class UserDeleteView(FormView):
    template_name = 'delete_profile.html'

    form_class = UserDeleteForm

    success_url = "/users/profile_deleted_confirm/"

    def form_valid(self, form):
        user = self.request.user
        user.is_active = False
        user.save()
        return super(UserDeleteView, self).form_valid(form)
