from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import VoteForm,  RegistrationForm
import random

import hashlib

def generate_hash_key():
    return hashlib.sha256(str(random.randint(1, 1000)).encode()).hexdigest()

def home(request):
    return render(request, 'voting/home.html')  # Make sure the template name matches the file name

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user  # Associate user with the authenticated user
            user.save()
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'voting/register.html', {'form': form})

@login_required
def vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.voter = request.user.voter
            vote.hash_key = generate_hash_key()  # Implement hash key generation
            vote.save()
            return redirect('thank_you')
    else:
        form = VoteForm()
    return render(request, 'voting/vote.html', {'form': form})

@login_required
def thank_you(request):
    return render(request, 'voting/thank_you.html')



