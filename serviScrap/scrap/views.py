from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View

from .forms import PersonalForm
from .models import *

from django.db.models import Q


def scrap_table(request):
    goods = Goods.objects.all()
    return render(request, 'scrap/scrap_table.html', {'goods': goods})


# def scrap_run(request):
#     # goods = Goods.objects.all()
#     print(request.POST)
#     return render(request, 'scrap/scrap_settings.html')


def scrap_settings(request):
    form = PersonalForm()
    personal_data = Personal.objects.all()
    if request.POST:
        Personal.objects.update(login=request.POST.get('login'), password=request.POST.get('password'),
                                name_shop=request.POST.get('name_shop'), id_partner=request.POST.get('id_partner'),
                                city=request.POST.get('city'))

    return render(request, 'scrap/scrap_settings.html', {'personal_data': personal_data, 'form': form})

