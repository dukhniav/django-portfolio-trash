import datetime

from django.db import models
from django.utils import timezone

class CustomerType(models.Model):
    customer_type = ["individual", "business"]


class Customer(models.Model):
    customer_type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        name = ''
        if self.customer_type == "individual":
            name = f'{self.first_name} {self.last_name}'
        else:
            name = self.business_name
        return name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)