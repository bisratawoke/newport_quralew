from .views import ProductView,Authenticator
from django.urls import path
urlpatterns = [
    path('',ProductView.as_view()),
    path('auth/',Authenticator.as_view())
]
