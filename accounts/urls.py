from django.urls import path
from .views import *

urlpatterns = [
    path('signup',SignUpiew.as_view(),name="signup_page")
]
