from django import forms
from .models import Topic,Board,Post 

class TopicForm(forms.ModelForm):
	message=forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),max_length=4000)

	class Meta:
		model=Topic
		fields=['subject','message']
		# fields="__all__"

class BoardForm(forms.ModelForm):
	class Meta:
		model=Board
		fields=['name','description']

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['message',]