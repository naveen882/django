# Create your views here.
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseForbidden
import json
import os
from django.contrib.auth.models import User
from .forms import ArticleForm

def login(request):
	print "In login============="
	if request.method == 'POST':
		print "In login=========="
		form = ArticleForm(request.POST)
		print form
		if form.is_valid():
			print "valid=============="
			return HttpResponseRedirect('/thanks/')
		else:
			print "Invalid============"
	return render(request, 'name.html', {'form': form})

