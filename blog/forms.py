from django import forms
from blog.models import Article

class ArticleForm(forms.ModelForm):

    def clean(self): 
        cleaned_data = super().clean()     
          
        body = cleaned_data.get('body')

        if len(body) < 2: 
            self.add_error('body', 'Body must be longer than one character.')

        
        return cleaned_data 

    # def is_valid():
    #     pass 

    class Meta:
        model = Article
        fields = ('title', 'body', 'author',)