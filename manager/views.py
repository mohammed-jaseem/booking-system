from django.shortcuts import render, reverse
from web.models import *
from django.http import HttpResponseRedirect
from manager.forms import *
from main.functions import generate_form_errors


def index(request):
    
    return render(request,'manager/index.html')
