from django.db import models
from django.contrib.auth.models import User

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    nrc = models.CharField(max_length=20)
    blockchain = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.CharField(max_length=100)
    hash_key = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.voter.name} voted for {self.candidate}"
