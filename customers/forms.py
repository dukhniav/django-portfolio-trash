from django import forms
# from  localflavor.models import USStateField
from phone_field import PhoneField

from .models import Customer




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    is_business = forms.BooleanField(required=False, help_text="Is this customer a bussiness.")
    business_name = forms.CharField(max_length=50, required=False, help_text='Bussiness name.')
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    # address
    address_1 = forms.CharField(required=False,help_text="address", max_length=128)
    address_2 = forms.CharField(required=False,help_text="address cont'd", max_length=128)

    city = forms.CharField(required=False,help_text="city", max_length=64)
    # state = USStateField("state", default="OH")
    zip_code = forms.CharField(required=False,help_text="zip code", max_length=5)

    # contact
    phone_number = PhoneField(blank=False, help_text='Contact phone number')
    email = forms.EmailField(required=False,max_length=120, help_text='Required. Enter a valid email address.')



    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2')

