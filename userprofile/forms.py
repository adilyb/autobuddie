from django.forms import ModelForm
from userprofile.models import UserProfileModel

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfileModel
        exclude=("user","status", "created_on","updated_on","status")