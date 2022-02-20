from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import DeviceForm
from .networking import wake_on_lan


def home(request):
    return render(request, 'wakeonlan/home.html')


def wake(request):
    if request.method == 'POST':  # was submitted
        form = DeviceForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data.get('ip_address')
            mac = form.cleaned_data.get('mac_address')
            try:
                SUCCESS = wake_on_lan(ip, mac)
            except:
                SUCCESS = False
            if SUCCESS:
                messages.success(request, f"Sent WOL packet to device: {ip=}, {mac=}")
            else:
                messages.warning(request, f"Something went wrong with that request")
            return redirect('wol-home')
    else:
        form = DeviceForm()
    return render(request, 'wakeonlan/wake.html', {'form': form})
