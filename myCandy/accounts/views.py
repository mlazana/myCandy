# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'registration/login.html')