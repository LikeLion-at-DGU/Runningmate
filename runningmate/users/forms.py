from cProfile import label
from allauth.account.forms import SignupForm as accountform
from allauth.socialaccount.forms import SignupForm as socialaccountform

from django import forms
from .models import *


class CustomSignupForm(accountform):

    password1 = forms.CharField(
        min_length=8,
        label="비밀번호",
        widget=forms.PasswordInput(),
        
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(), 
        label="Confirm Password",
        )

    email = forms.CharField(
        max_length=40,
        label="이메일 주소",
        widget=forms.TextInput(  # HTML 에서 input tag임
            attrs={
                "type": "email",
                "placeholder": "you@example.com",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=10,
        label="성",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "홍",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=10,
        label="이름",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "길동",
            }
        ),
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        profile = Profile()
        profile.user = user
    #    profile.phone = self.cleaned_data["phone"]
    #    profile.mbti = self.cleaned_data["mbti"]
    #    profile.intro = self.cleaned_data["intro"]
        profile.save()
        return user

class SocialSignupForm(socialaccountform):
    password1 = forms.CharField(
        min_length=8,
        label="비밀번호",
        widget=forms.PasswordInput(),
        )
    password2 = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(), 
        label="Confirm Password",
        )

    email = forms.CharField(
        max_length=40,
        label="이메일 주소",
        widget=forms.TextInput(  # HTML 에서 input tag임
            attrs={
                "type": "email",
                "placeholder": "you@example.com",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=10,
        label="성",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "홍",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=10,
        label="이름",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "길동",
            }
        ),
    )

    def save(self, request):
        user = super(SocialSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        profile = Profile()
        profile.user = user
    #    profile.phone = self.cleaned_data["phone"]
    #    profile.mbti = self.cleaned_data["mbti"]
    #    profile.intro = self.cleaned_data["intro"]
        profile.save()
        return user