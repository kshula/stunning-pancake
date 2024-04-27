from django import forms
from .models import Voter, Vote

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Voter
        fields = ['name', 'nrc']
        labels = {
            'name': 'Full Name',
            'nrc': 'National Registration Card (NRC)'
        }

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['candidate']
        labels = {
            'candidate': 'Select Candidate'
        }

    def __init__(self, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        # Customize candidate choices based on your requirements
        self.fields['candidate'].widget = forms.Select(choices=[
            ('Donald Trump', 'Donald Trump'),
            ('Joe Biden', 'Joe Biden')
        ])