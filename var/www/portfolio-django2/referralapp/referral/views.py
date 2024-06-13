from django.shortcuts import render, redirect
from .models import Person, Referral
from .forms import PersonForm, ReferralForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'referral/home.html')

@login_required
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'referral/person_list.html', {'persons': persons})

@login_required
def person_detail(request, id):
    person = Person.objects.get(pk=id)
    referrals = person.referral_set.all()
    return render(request, 'referral/person_detail.html', {'person': person, 'referrals': referrals})

@login_required
def person_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = PersonForm()
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(instance=person)
        return render(request, 'referral/person_form.html', {'form': form})
    else:
        if id == 0:
            form = PersonForm(request.POST)
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')

@login_required
def person_delete(request, id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect('person_list')

@login_required
def referral_list(request):
    referrals = Referral.objects.all()
    return render(request, 'referral/referral_list.html', {'referrals': referrals})

@login_required
def referral_detail(request, id):
    referral = Referral.objects.get(pk=id)
    return render(request, 'referral/referral_detail.html', {'referral': referral})

@login_required
def referral_form(request, person_id, id=0):
    person = Person.objects.get(pk=person_id)
    if request.method == 'GET':
        if id == 0:
            form = ReferralForm(initial={'person': person})
        else:
            referral = Referral.objects.get(pk=id, person=person)
            form = ReferralForm(instance=referral)
        return render(request, 'referral/referral_form.html', {'form': form})
    else:
        if id == 0:
            form = ReferralForm(request.POST, request.FILES)
        else:
            referral = Referral.objects.get(pk=id, person=person)
            form = ReferralForm(request.POST, request.FILES, instance=referral)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.person = person
            referral.save()
            if id == 0:
                return redirect('person_detail', id=person_id)
            else:
                return redirect('referral_detail', id=referral.id)

@login_required
def referral_delete(request, id):
    referral = Referral.objects.get(pk=id)
    referral.delete()
    return redirect('referral_list')
