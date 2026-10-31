from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        required=True, widget=forms.DateInput(attrs={"type": "date"})
    )

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

            UserProfile.objects.create(
                user=user, date_of_birth=self.cleaned_data["date_of_birth"]
            )

        return user
