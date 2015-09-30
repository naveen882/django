from django.conf import settings
settings.configure()
from django.contrib.auth.models import User
user = User.objects.create_user('tom', 'tom@tom.com', 'tompassword')
user.save()
user = User.objects.create_user('jerry', 'jerry@jerry.com', 'jerrypassword')
user.save()
