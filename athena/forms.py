from django import forms

class UploadForm(forms.Form):
	file_field = forms.FileField(label='', widget=forms.ClearableFileInput(attrs={'multiple': True, 'accept': "image/*"}))