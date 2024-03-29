"""
URL mapping for  for the user API
"""
from django.urls import path

from user import views
from user.views import ManageUserView


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me'),





]
