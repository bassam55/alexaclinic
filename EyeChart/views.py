from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from EyeChart.forms import NewPatientForm
from EyeChart.models import Patient
# Create your views here.

def welcomepage(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'EyeChart/test.html')

def index2(request):
    return render(request, 'EyeChart/test2.html')

def paitents(request):
    form = NewPatientForm()

    if request.method == "POST":
        form = NewPatientForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return welcomepage(request)
        else:
            print('invalid form')
    return render(request, 'EyeChart/patientform.html', {'form':form})

def paitents2(request):
    form = NewPatientForm()

    if request.method == "POST":
        form = NewPatientForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return welcomepage(request)
        else:
            print('invalid form')
    return render(request, 'EyeChart/patientform2.html', {'form':form})


def displaytable(request):
    patients_table = Patient.objects.order_by('id')
    data_dict = {'table': patients_table }
    return  render(request, 'EyeChart/table.html', context=data_dict)
