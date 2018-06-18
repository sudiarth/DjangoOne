from django.shortcuts import render, redirect
from . import models as m
from django.contrib import messages

def index(request):
    context = {
        'bills' : m.BillItem.objects.all().order_by('-created_at')
    }
    return render(request, 'bill_tracker/index.html', context)

def create_bill(request):
    if request.method == 'POST':
        try:
            bill_item = m.BillItem()
            bill_item.description = request.POST['html_description']
            bill_item.amount = request.POST['html_amount']
            bill_item.save()

            request.session['bill_description'] = bill_item.description
            
        except:
            messages.error(request, 'Invalid input')

    return redirect('bill_tracker:index')

def delete_bill(request, bill_id):
    bill = m.BillItem.objects.get(id=bill_id)
    bill.delete()
    return redirect('bill_tracker:index')

def edit_bill(request, bill_id):
    bill = m.BillItem.objects.get(id=bill_id)

    if request.method == 'POST':
        try:
            bill.description = request.POST['html_description']
            bill.amount = request.POST['html_amount']
            bill.save()
        except:
            messages.error(request, 'Invalid input')
            return redirect('bill_tracker:edit_bill', bill_id=bill.id)

        return redirect('bill_tracker:index')

    context = {
        'bill' : bill
    }

    return render(request, 'bill_tracker/edit.html', context)