from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=50)
	subject = forms.CharField(max_length=100)
	sender = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'copy_flag'}))
	copy = forms.BooleanField(required=False)