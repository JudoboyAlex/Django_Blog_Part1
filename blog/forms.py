from django import forms
from blog.models import Article
from django.forms import CharField, PasswordInput, Form, ModelForm

class CommentForm(forms.ModelForm):

    def clean(self): 
        cleaned_data = super().clean()     
        body = cleaned_data.get('body')

        if len(body) < 2: 
            self.add_error('body', 'Body must be longer than one character.')      
        return cleaned_data 

    class Meta:
        model = Article
        fields = ['title', 'body', 'author',]

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'body', 'author']