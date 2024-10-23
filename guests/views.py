from django.shortcuts import render, redirect, get_object_or_404
from .models import Guest
from .forms import GuestForm  # Create this form

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'guests/guest_list.html', {'guests': guests})

def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    return render(request, 'guests/guest_detail.html', {'guest': guest})

def guest_create(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm()
    return render(request, 'guests/guest_form.html', {'form': form})

def guest_update(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "POST":
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'guests/guest_form.html', {'form': form})

def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "POST":
        guest.delete()
        return redirect('guest_list')  # Redirect to the guest list after deletion
    return render(request, 'guests/guest_confirm_delete.html', {'guest': guest})