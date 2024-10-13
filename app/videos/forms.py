from django import forms

class VideoGenerationForm(forms.Form):
    title = forms.CharField(max_length=255)
    script = forms.CharField(widget=forms.Textarea)
