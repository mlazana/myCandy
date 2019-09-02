# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.shortcuts import render, HttpResponse
from .forms import valueForm

def home(request):
    if request.method == "POST":
        form = valueForm(request.POST)
        money = int(form['moneyValue'].value())

        result = money // 5
        extra = result // 3

        if extra > 0 :
            result += extra

        return  render(request, 'result.html',{'result':result, 'money': money})
    else:
        return render(request, 'home.html')

