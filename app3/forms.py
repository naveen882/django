from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['candidate_id', 'created_by', 'modified_by','tenant_id','rank']
