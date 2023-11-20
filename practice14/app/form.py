from django import forms 

class PostForm(forms.Form):
    author_post = forms.CharField(label='Author post')
    title_post = forms.CharField(label='Title post')
    text_post = forms.CharField(label='Text post',widget=forms.Textarea)
    likes_post = forms.IntegerField(label='Введите сколько лайков изначально будет у поста ' )