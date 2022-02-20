from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .forms import DeviceForm


def home(request):
    return HttpResponse('<h1>Wake on LAN</h1>')


def wake(request):
    if request.method == 'POST':  # was submitted
        form = DeviceForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data.get('ip_address')
            mac = form.cleaned_data.get('mac_address')
            messages.success(request, f'Submitted wake-on-lan request for device: {ip=}, {mac=}')
    else:
        form = DeviceForm()
    return render(request, 'wakeonlan/wake.html', {'form': form})
