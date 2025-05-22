from django import forms

from .models import Comment, Incident


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-area-class form-control'}))
    
    class Meta:
        model = Comment
        fields = ('comment',)
        

class IncidentForm(forms.ModelForm):
    form_of_corruption = forms.CharField(max_length=150)
    location = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-area-class form-control'}))
    email = forms.EmailInput()

    class Meta:
        model = Incident
        fields = '__all__'
