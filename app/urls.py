from .views import AboutUsView, UserView, UserUpdateView, ProductView, AddUserView, AddProductView, ProductUpdateView 
from django.urls import path

urlpatterns = [
    path('about/', AboutUsView.as_view(), name='about'),
    path('user/', UserView.as_view(), name='user'),
    path('product/', ProductView.as_view(), name='product'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('add_user/', AddUserView.as_view(), name='add_user'),
    path('user_update/<int:id>/', UserUpdateView.as_view(), name="user_update"),
    path('product_update/<int:id>/', ProductUpdateView.as_view(), name="product_update")
]