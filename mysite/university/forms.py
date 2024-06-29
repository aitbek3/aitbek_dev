from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import UserProfileProfessor, UserProfileStudent, Schedule


class CustomSignupForm(SignupForm):
    last_name = forms.CharField(max_length=100, label=_('last_name'))
    country = forms.CharField(max_length=100, label=_('Country'))
    age = forms.IntegerField(label=_('Age'))
    phone_number = forms.CharField(max_length=20, label=_('Phone Number'))

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        phone_number = phone_number.replace(" ", "")

        if len(phone_number) != 9 or not phone_number.isdigit():
            raise ValidationError(_('Invalid phone number format. Please use 11-digit format without spaces'))

        return phone_number

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        last_name = self.cleaned_data['last_name']
        country = self.cleaned_data['country']
        age = self.cleaned_data['age']
        phone_number = "+996 " + self.cleaned_data['phone_number']

        if hasattr(user, 'userprofile'):
            profile = user.userprofile
        else:
            profile = UserProfileProfessor(user=user)

        profile.last_name = last_name
        profile.country = country
        profile.age = age
        profile.phone_number = phone_number
        profile.save()

        return user


class CustomSignupForm(SignupForm):
    last_name = forms.CharField(max_length=100, label=_('last_name'))
    phone_number = forms.CharField(max_length=20, label=_('Phone Number'))

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        phone_number = phone_number.replace(" ", "")

        if len(phone_number) != 9 or not phone_number.isdigit():
            raise ValidationError(_('Invalid phone number format. Please use 11-digit format without spaces'))

        return phone_number

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        last_name = self.cleaned_data['last_name']
        phone_number = "+996 " + self.cleaned_data['phone_number']

        if hasattr(user, 'userprofile'):
            profile = user.userprofile
        else:
            profile = UserProfileStudent(user=user)

        profile.last_name = last_name
        profile.phone_number = phone_number
        profile.save()

        return user


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

