from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [

    path('', views.CustomerView.as_view(), name='customer_list'),
    path('new/', views.new_customer, name='new_customer'),
    # path('<int:customer_id>/edit/', views.detail, name='detail'),
    # path('<int:customer_id>/view/', views.detail, name='detail'),

]