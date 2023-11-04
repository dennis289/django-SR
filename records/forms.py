from django import forms
from django.forms import ModelForm
from studentRecord.models import student
from finances.models import feePayments, feeBalance


class studentForm(ModelForm):
    class Meta:
           model= student
           fields = ('__all__')
           
           labels = {
                 'Full_name':'',
                 'reg_no':'',
                 'email':'',
                 'contact':'',
                 'registration':'',
                 
           }

           widgets= {
                 'Full_name':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Full name'}),
                 'reg_no':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Registration number'}),
                 'email':forms.EmailInput(attrs={'class':'form-control' ,'placeholder':'Email'}),
                 'contact':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Contact'}),
                 
           }


class feePaymentsForm(ModelForm):
      class Meta:
            model= feePayments
            fields = ('__all__')

class feeBalanceForm(ModelForm):
      class Meta:
            model = feeBalance
            fields = '__all__'

class compositeForm(forms.Form):
     fee_payment=feePaymentsForm()
     fee_balance=feeBalanceForm()
     
