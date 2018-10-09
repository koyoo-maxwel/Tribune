from django import forms
from .models import Article

class NewsLetterForm(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=30)
    last_name = forms.CharField(label='Lsat Name',max_length=30)

    email = forms.EmailField(label='Email')

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }