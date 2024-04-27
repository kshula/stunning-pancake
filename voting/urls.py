from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home page
    path('register/', views.register, name='register'),  # URL for voter registration
    path('vote/', views.vote, name='vote'),  # URL for casting a vote
    path('thank-you/', views.thank_you, name='thank_you'),  # URL for thank you page
]
