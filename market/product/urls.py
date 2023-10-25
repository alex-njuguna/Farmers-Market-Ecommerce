from django.urls import path

from .views import home, create_product, product_details, update_product, delete_product


app_name = "product"

urlpatterns = [
    path("", home, name="home"),
    path('create_product/', create_product, name='create_product'),
    path('product_details/<int:id>/', product_details, name='product_details'),
    path('update_product/<int:id>', update_product, name='update_product'),
    path('delete_product/<int:id>', delete_product, name='delete_product')
]