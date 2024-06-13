from django import forms
from .models import Person, Referral

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth']
        labels ={
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'date_of_birth': 'Date Of Birth'
        }

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referral_date', 'referrer_name', 'reason', 'note', 'document']
        labels ={
            'referral_date': 'Referral Date',
            'referrer_name': 'Referrer Name',
            'reason': 'Reason',
            'note': 'Note',
            'document':'Upload Document'
        }

    def __init__(self, *args, **kwargs):
        super(ReferralForm,self).__init__(*args, **kwargs)
        self.fields['note'].required = False
        self.fields['document'].required = False
