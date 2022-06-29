from allauth.account.forms import SignupForm as accountform
from allauth.socialaccount.forms import SignupForm as socialaccountform

from django import forms
from .models import *


class CustomSignupForm(accountform):
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
    phone = forms.CharField(
        max_length=13,
        min_length=13,
        label="휴대전화 번호",
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "placeholder": "010-0000-0000",
            }
        ),
    )
    mbti = forms.CharField(
        max_length=4,
        min_length=4,
        label="MBTI",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "ESTJ",
            }
        ),
    )
    intro = forms.CharField(
        max_length=100,
        min_length=0,
        label="한 줄 소개",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "한 줄 소개",
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
        profile.phone = self.cleaned_data["phone"]
        profile.mbti = self.cleaned_data["mbti"]
        profile.intro = self.cleaned_data["intro"]
        profile.save()
        return user

class SocialSignupForm(socialaccountform):
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
    phone = forms.CharField(
        max_length=13,
        min_length=0,
        label="휴대전화 번호",
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "placeholder": "010-0000-0000",
            }
        ),
    )
    mbti = forms.CharField(
        max_length=4,
        min_length=4,
        label="MBTI",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "ESTJ",
            }
        ),
    )
    intro = forms.CharField(
        max_length=100,
        min_length=0,
        label="한 줄 소개",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "한 줄 소개",
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
        profile.phone = self.cleaned_data["phone"]
        profile.mbti = self.cleaned_data["mbti"]
        profile.intro = self.cleaned_data["intro"]
        profile.save()
        return user