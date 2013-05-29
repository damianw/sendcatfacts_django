from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

def index(request):
	if request.method == 'POST':
		phone = request.POST['phone']
	return render(request, 'sendcatfacts_django/index.html')