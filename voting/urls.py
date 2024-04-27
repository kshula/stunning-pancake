from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register_voter'),
    path('vote/', views.vote, name='cast_vote'), # URL for thank you page
]
