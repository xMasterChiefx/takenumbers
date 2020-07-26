from django.shortcuts import render, redirect, get_object_or_404
from .models import Bestellnummer
from .forms import BestellnummerForm
from django.db.models import Count, F
from django.utils import timezone


# Create your views here.

def index(request):
    nums = Bestellnummer.objects.filter(archieved=False)
    nums = nums.filter(completed__isnull=False)
    return render(request, 'takenumbers/home.html', {'nums':nums})


def nextnumber(request):
    if request.method == 'GET':
        lastbnum = Bestellnummer.objects.all().count()
        lastbnum = lastbnum +1
        return render(request, 'takenumbers/input.html', {'form':BestellnummerForm(initial={'bnum': lastbnum})})
    else:
        try:
            form = BestellnummerForm(request.POST)
            newbnumber = form.save(commit=False)
            newbnumber.save()
            return redirect('takenumbers:nextnumber')
        except ValueError:
            return render(request, 'takenumbers/input.html', {'form':BestellnummerForm(),'error':'Bad Data passed in'})


def workingnumber(request):
    if request.method == 'GET':
        nums = Bestellnummer.objects.filter(completed__isnull=True)
        return render(request, 'takenumbers/working.html', {'nums':nums})
    else:
        try:
            #form = BestellnummerForm(request.POST)
            #newbnumber = form.save(commit=False)
            newbnumber.save()
            return redirect('workingnumber')
        except ValueError:
            return render(request, 'takenumbers/working.html', {'form':BestellnummerForm(),'error':'Bad Data passed in'})


def bncheck(request,nums_pk):
    nums = get_object_or_404(Bestellnummer, pk=nums_pk)
    if request.method == 'GET':
        nums = Bestellnummer.objects.filter(completed__isnull=True)
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo':todo,'form':form})


def dashboard(request):
    if request.method == 'GET':
        nums = Bestellnummer.objects.all()
        nums_count = Bestellnummer.objects.count()
        nums_working = Bestellnummer.objects.filter(completed__isnull=True).count()
        return render(request, 'takenumbers/dashboard.html', {'nums':nums,'nums_count':nums_count, 'nums_working':nums_working})


def bnarchive(request):
    pass


def bnready(request,num_pk):
    num = get_object_or_404(Bestellnummer, pk=num_pk)
    if request.method == 'POST':
        num.completed = timezone.now()
        num.save()
        return redirect('takenumbers:workingnumber')


def bndelete(request):
    pass


def alldelete(request):
    if request.method == 'GET':
        return render(request, 'takenumbers/alldelete.html')
    else:
        try:
            nums = Bestellnummer.objects.all()
            nums.delete()
            return redirect('takenumbers:dashboard')
        except ValueError:
            return render(request, 'takenumbers/dashboard.html', {'error':'Bad Data passed in'})

def takeout(request):
    if request.method == 'GET':
        nums = Bestellnummer.objects.filter(completed__isnull=False)
        nums = nums.filter(archieved=False)
        return render(request, 'takenumbers/takeout.html', {'nums':nums})
    else:
        try:
            #form = BestellnummerForm(request.POST)
            deletenumber = form.delete(commit=False)
            deletenumber.delete()
            return redirect('takenumbers:workingnumber')
        except ValueError:
            return render(request, 'takenumbers/takeout.html', {'nums':BestellnummerForm(),'error':'Bad Data passed in'})


def takedelete(request,num_pk):
    num = get_object_or_404(Bestellnummer, pk=num_pk)
    if request.method == 'POST':
        num.archieved = True
        num.save()
        return redirect('takenumbers:takeout')

