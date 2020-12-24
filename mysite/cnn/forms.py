from django import forms

class LinkForm(forms.Form):
	title = forms.CharField(label = 'title', max_length=150)
	image = forms.ImageField(label= 'image')
	desc = forms.CharField(label='description')
	category = forms.CharField(label='category', max_length=75)
