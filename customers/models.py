import datetime

from django.db import models
from django.utils import timezone
from phone_field import PhoneField


class CustomerType(models.Model):
    customer_type = ["individual", "business"]


class Customer(models.Model):
    is_business = models.BooleanField(default=False)
    business_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_1   = models.CharField(max_length=200)
    address_2= models.CharField(max_length=200, default='address')
    city= models.CharField(max_length=200, default='address')
    # state = models.CharField(max_length=200)
    zip_code= models.CharField(max_length=200, default='address')
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    email= models.EmailField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        name = ''
        if self.is_business:
            name = self.business_name
        else:
            name = f'{self.first_name} {self.last_name}'
        return name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)