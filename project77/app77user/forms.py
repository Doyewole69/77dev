from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, ForexDenModel

class CustomUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("first_name", "last_name",
                  "email", "username", "password1", "password2")

class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class ForexDenForm(forms.ModelForm):

    class Meta:

        model = ForexDenModel

        fields = [
            "Balance","Earning","Last_Deposit","Pending_Withdrawal","Referals","Earned_Commission",
        ]