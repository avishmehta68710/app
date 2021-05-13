from django import forms
from .models import *

class AdminModel(forms.ModelForm):
    
    class Meta:
        model = admin_model
        fields = ['advisor_name','advisor_image','advisor_id']
        
class RegisterUser(forms.ModelForm):
    
    class Meta:
        model = user_models
        fields = ['name','email','password']
        
class Loginuser(forms.ModelForm):
    
    class Meta:
        model = login_user
        fields = ['email','password']
        
class BookCall(forms.ModelForm):
    
    class Meta:
        model = can_book_call
        fields = ['date','booking_id']