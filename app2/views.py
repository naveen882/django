# Create your views here.
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseForbidden
import json
import os
from django.contrib.auth.models import User


