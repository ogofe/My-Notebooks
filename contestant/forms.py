# # creating the user creation form
# # adding custom fields such as
# # phonenumber, picture and state

# # imports
from django import forms
from django.contrib.auth.forms import (
    ReadOnlyPasswordHashField,
    UserCreationForm
    )
from .models import Account


# # create a new user

class Create(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username', 'email',)
        
class Profile(forms.ModelForm):
    class Meta:
        model = Account
        fields = (
            'phone',
            'image'
        )
    def save(self, commit=True):
        "Complete profile"
        phone = self.cleaned_data['phone']
        image = self.cleaned_data['image']