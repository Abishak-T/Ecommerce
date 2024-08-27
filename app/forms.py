from django.forms import Form,ModelForm
from app.models import AppModel,SubModel,SignupModel


class AppForm(ModelForm):
    class Meta:
        model=AppModel
        fields="__all__"
        
        
class SubForm(ModelForm):
    class Meta:
        model=SubModel
        fields="__all__"
        
        
class SignupForm(ModelForm):
    class Meta:
        model=SignupModel
        fields="__all__"        