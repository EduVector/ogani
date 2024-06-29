from django import forms
from ckeditor.widgets import CKEditorWidget

from apps.blog.models import Article


class ArticleAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Article
        fields = '__all__'