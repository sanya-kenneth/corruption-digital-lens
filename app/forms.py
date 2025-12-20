from django import forms

from .models import (Comment, Incident, Feedback, LIKERT_CHOICES)


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
        
# ######################################################
# #
# # Questionnaire forms
# #
# #######################################################

from django import forms
from .models import SystemResponse, PublicResponse, EmployeeResponse

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.__class__ == forms.Select and field.choices:
                field.widget = forms.RadioSelect(choices=field.choices)
            if name == 'comment':
                field.widget = forms.Textarea(attrs={'rows': 4})

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('gender') == 3 and not cleaned_data.get('gender_other'):
            self.add_error('gender_other', 'Please specify if others is selected.')
        if cleaned_data.get('religion') == 5 and not cleaned_data.get('religion_other'):
            self.add_error('religion_other', 'Please specify if others is selected.')
        return cleaned_data

class SystemForm(BaseForm):
    class Meta:
        model = SystemResponse
        exclude = ['created_at']

class PublicForm(BaseForm):
    class Meta:
        model = PublicResponse
        exclude = ['created_at']

class EmployeeForm(BaseForm):
    class Meta:
        model = EmployeeResponse
        exclude = ['created_at']
