from django.urls import path
from accounts.views import register_view
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    
]