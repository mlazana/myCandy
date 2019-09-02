# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.shortcuts import render, HttpResponse
from .forms import valueForm

def home(request):
    if request.method == "POST":
        form = valueForm(request.POST)
        text = form['moneyValue'].value()
        return  render(request, 'result.html',{'result':text})
    else:
        return render(request, 'home.html')

