from django.shortcuts import render
from .models import Patient
from .forms import PatientCheck

# Create your views here.
def patient_check(request):
    result = None
    if request.method == 'POST':
        form = PatientCheck(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            result = Patient.objects.filter(first_name__iexact=first, last_name__iexact=last)
    else:
        form = PatientCheck()

    return render(request, 'patient_check.html', {'form': form, 'result': result})