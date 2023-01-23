from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def about(request):
	return render(request, 'generator/about.html')


def password(request):
	
	chars = list('abcdefghijklmnopqrstuvwxyz')
	if request.GET.get('uppercase'):
		chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		chars.extend(list('±!@#$%^&*()_-+=}][{:;|,<>./?~'))
	if request.GET.get('numbers'):
		chars.extend(list('1234567890'))
	length = int(request.GET.get('length', default=12))
	thePassword = ''
	for x in range(length):
		thePassword += random.choice(chars)
	return render(request, 'generator/password.html', {'password': thePassword})