from django.db import models
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import fields


class Article(models.Model):
	candidate_id = models.IntegerField(null=True,unique=True)
	created_by = models.IntegerField()
	modified_by = models.IntegerField(null=True)
	tenant_id = models.IntegerField(null=True)
	rank = models.IntegerField(null=True)

	class Meta:
		db_table = 'Article'


