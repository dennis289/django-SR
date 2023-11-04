from django.shortcuts import render,reverse
from .forms import studentForm, compositeForm
from django.http import HttpResponseRedirect


def add_student (request):
        submitted = False
        if request.method == 'POST':
                form = studentForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect(reverse('add_student') + '?submitted=true')

        else:       
                form = studentForm
                if 'submitted' in request.GET:
                        submitted = True

        return render (request, "records/add_student.html", {'form': form, 'submitted': submitted})


def finances(request):
    submitted = False
    if request.method == 'POST':
        form = compositeForm(request.POST)
        if form.is_valid(): 
            fee_payment = form.cleaned_data['fee_payment']
            fee_balance = form.cleaned_data['fee_balance'] 
            fee_payment.save(commit=False)
            fee_balance.save(commit=False)
            return HttpResponseRedirect(reverse('finances') + '?submitted=true')
    else:
        form = compositeForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "records/finances.html", {'form': form, 'submitted': submitted})
