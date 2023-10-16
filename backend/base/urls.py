from django.urls import path
from . import views 

# from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('', views.getRoutes, name='routes'),

    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>/', views.getProductDetails, name='product-details'),

    path('users/', views.getUsers, name='users'),
    path('users/profile/', views.getUserProfile, name='user-profile'),

    # path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      # it just return referesh and access, so we have to overwrite it 
    path('users/login/', views.myTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='register'),
]
