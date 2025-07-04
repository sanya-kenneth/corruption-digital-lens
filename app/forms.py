from django import forms

from .models import Comment, Incident, Feedback


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-area-class form-control'}))
    act = forms.CharField(widget=forms.TextInput(attrs={"type":"hidden", "id":"modal-input", "name":"modal-input"}))

    class Meta:
        model = Comment
        fields = ('comment',)


class IncidentForm(forms.ModelForm):
    form_of_corruption = forms.CharField(max_length=150)
    location = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-area-class form-control'}))
    email = forms.EmailField(required=False)

    class Meta:
        model = Incident
        fields = '__all__'
        

class FeedbackForm(forms.ModelForm):
    # form_of_corruption = forms.CharField(max_length=150)
    # location = forms.CharField(max_length=150)
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-area-class form-control'}))
    # email = forms.EmailInput()
    name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={"id":"name", "name":"name"}), required=False, label="Your Name(optional)")
    email = forms.CharField(widget=forms.TextInput(attrs={"id":"email", "name":"email"}), required=False, label="Your Email(optional)")
    feedback_type = forms.ChoiceField(widget=forms.Select(attrs={"id":"category", "name":"category"}), 
                                      choices=Feedback.FEEDBACK_CHOICES)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-area-class form-control', 
                                                           "placeholder":"Share your thoughts, suggestions, or report any issues..."}))

    class Meta:
        model = Feedback
        fields = '__all__'
