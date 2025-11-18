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

# class RadioSelectLikert(forms.RadioSelect):
#     def __init__(self, *args, **kwargs):
#         kwargs['choices'] = LIKERT_CHOICES
#         super().__init__(*args, **kwargs)

# class RespondentForm(forms.ModelForm):
#     class Meta:
#         model = Respondent
#         fields = '__all__'
#         exclude = ['created_at', 'is_post_intervention']  # Set is_post in view
#         widgets = {
#             'gender': forms.RadioSelect,
#             'age': forms.RadioSelect,
#             'education': forms.RadioSelect,
#             'religion': forms.RadioSelect,
#             'experience': forms.RadioSelect,
#             'family_size': forms.RadioSelect,
#             'marital_status': forms.RadioSelect,
#             'income': forms.RadioSelect,
#             'org_age': forms.RadioSelect,
#             'org_size': forms.RadioSelect,
#             'org_location': forms.RadioSelect,
#             'org_category': forms.TextInput(attrs={'placeholder': 'e.g., Education, Security, Judiciary etc'}),
#             'religion_other': forms.TextInput(attrs={'placeholder': 'Specify if other'}),
#         }

# class EconomicForm(forms.ModelForm):
#     adequate_income = forms.IntegerField(widget=RadioSelectLikert)
#     economic_freedom = forms.IntegerField(widget=RadioSelectLikert)
#     inflation_affect = forms.IntegerField(widget=RadioSelectLikert)
#     international_trade = forms.IntegerField(widget=RadioSelectLikert)
#     national_trade = forms.IntegerField(widget=RadioSelectLikert)
    
#     class Meta:
#         model = EconomicResponse
#         exclude = ['respondent']

# class SocialForm(forms.ModelForm):
#     social_distress = forms.IntegerField(widget=RadioSelectLikert)
#     social_exclusion = forms.IntegerField(widget=RadioSelectLikert)
#     religious_beliefs = forms.IntegerField(widget=RadioSelectLikert)
#     male_dominance = forms.IntegerField(widget=RadioSelectLikert)
#     middle_class_life = forms.IntegerField(widget=RadioSelectLikert)
#     value_education = forms.IntegerField(widget=RadioSelectLikert)
#     low_job_intensity = forms.IntegerField(widget=RadioSelectLikert)
    
#     class Meta:
#         model = SocialResponse
#         exclude = ['respondent']

# class PoliticalForm(forms.ModelForm):
#     rule_of_law = forms.IntegerField(widget=RadioSelectLikert)
#     state_land_control = forms.IntegerField(widget=RadioSelectLikert)
#     democracy_practice = forms.IntegerField(widget=RadioSelectLikert)
#     political_rights = forms.IntegerField(widget=RadioSelectLikert)
#     civil_liberties = forms.IntegerField(widget=RadioSelectLikert)
#     fair_elections = forms.IntegerField(widget=RadioSelectLikert)
#     political_stability = forms.IntegerField(widget=RadioSelectLikert)
#     policy_framework = forms.IntegerField(widget=RadioSelectLikert)
    
#     class Meta:
#         model = PoliticalResponse
#         exclude = ['respondent']

# class DigitalForm(forms.ModelForm):
#     digital_infra_avail = forms.IntegerField(widget=RadioSelectLikert)
#     access_computers = forms.IntegerField(widget=RadioSelectLikert)
#     support_infra = forms.IntegerField(widget=RadioSelectLikert)
#     invest_policy = forms.IntegerField(widget=RadioSelectLikert)
#     improves_work = forms.IntegerField(widget=RadioSelectLikert)
#     frequent_use = forms.IntegerField(widget=RadioSelectLikert)
    
#     class Meta:
#         model = DigitalResponse
#         exclude = ['respondent']

# class ParticipationForm(forms.ModelForm):
#     council_meetings = forms.IntegerField(widget=RadioSelectLikert)
#     discuss_policies = forms.IntegerField(widget=RadioSelectLikert)
#     contribute_services = forms.IntegerField(widget=RadioSelectLikert)
#     public_info = forms.IntegerField(widget=RadioSelectLikert)
#     decision_making = forms.IntegerField(widget=RadioSelectLikert)
    
#     class Meta:
#         model = ParticipationResponse
#         exclude = ['respondent']

# class CorruptionForm(forms.ModelForm):
#     # Bribery
#     public_bribes = forms.IntegerField(widget=RadioSelectLikert)
#     request_gifts = forms.IntegerField(widget=RadioSelectLikert)
#     convenience_bribes = forms.IntegerField(widget=RadioSelectLikert)
#     faster_services = forms.IntegerField(widget=RadioSelectLikert)
#     concealment_bribes = forms.IntegerField(widget=RadioSelectLikert)
#     # Nepotism
#     use_facilities_family = forms.IntegerField(widget=RadioSelectLikert)
#     no_public_ads = forms.IntegerField(widget=RadioSelectLikert)
#     same_tribe = forms.IntegerField(widget=RadioSelectLikert)
#     tribe_promotions = forms.IntegerField(widget=RadioSelectLikert)
#     unequal_pay = forms.IntegerField(widget=RadioSelectLikert)
#     unqualified_employ = forms.IntegerField(widget=RadioSelectLikert)
#     # Favoritism
#     low_price_assets = forms.IntegerField(widget=RadioSelectLikert)
#     favor_friends = forms.IntegerField(widget=RadioSelectLikert)
#     no_demote_friends = forms.IntegerField(widget=RadioSelectLikert)
#     political_appoint = forms.IntegerField(widget=RadioSelectLikert)
#     sex_discrimination = forms.IntegerField(widget=RadioSelectLikert)
#     same_religion = forms.IntegerField(widget=RadioSelectLikert)
#     # Embezzlement
#     private_work_hours = forms.IntegerField(widget=RadioSelectLikert)
#     theft_properties = forms.IntegerField(widget=RadioSelectLikert)
#     theft_funds = forms.IntegerField(widget=RadioSelectLikert)
#     alter_reports = forms.IntegerField(widget=RadioSelectLikert)
#     evade_taxes = forms.IntegerField(widget=RadioSelectLikert)
#     private_use_resources = forms.IntegerField(widget=RadioSelectLikert)
    
#     comments = forms.Textarea(attrs={'rows': 4, 'placeholder': 'Other Comments'})
    
#     class Meta:
#         model = CorruptionResponse
#         exclude = ['respondent']



# #######################################
# #New forms
# #
# ######################################

# # forms.py
# from django import forms
# from .models import (
#     Respondent, EconomicResponse, SocialResponse, PoliticalResponse,
#     DigitalResponse, ParticipationResponse, CorruptionResponse,
#     INITIAL_CORRUPTION_LABELS, POST_CORRUPTION_LABELS
# )

# # # Custom Likert Radio Widget (assuming you have this)
# # from your_app.widgets import RadioSelectLikert  # Replace with your actual import


# # === 1. BASELINE FORM (Pre-intervention) ===
# class BaselineCorruptionForm(forms.ModelForm):
#     # All fields use same Likert scale
#     public_bribes = forms.IntegerField(widget=RadioSelectLikert)
#     request_gifts = forms.IntegerField(widget=RadioSelectLikert)
#     convenience_bribes = forms.IntegerField(widget=RadioSelectLikert)
#     faster_services = forms.IntegerField(widget=RadioSelectLikert)
#     concealment_bribes = forms.IntegerField(widget=RadioSelectLikert)

#     use_facilities_family = forms.IntegerField(widget=RadioSelectLikert)
#     no_public_ads = forms.IntegerField(widget=RadioSelectLikert)
#     same_tribe = forms.IntegerField(widget=RadioSelectLikert)
#     tribe_promotions = forms.IntegerField(widget=RadioSelectLikert)
#     unequal_pay = forms.IntegerField(widget=RadioSelectLikert)
#     unqualified_employ = forms.IntegerField(widget=RadioSelectLikert)

#     low_price_assets = forms.IntegerField(widget=RadioSelectLikert)
#     favor_friends = forms.IntegerField(widget=RadioSelectLikert)
#     no_demote_friends = forms.IntegerField(widget=RadioSelectLikert)
#     political_appoint = forms.IntegerField(widget=RadioSelectLikert)
#     sex_discrimination = forms.IntegerField(widget=RadioSelectLikert)
#     same_religion = forms.IntegerField(widget=RadioSelectLikert)

#     private_work_hours = forms.IntegerField(widget=RadioSelectLikert)
#     theft_properties = forms.IntegerField(widget=RadioSelectLikert)
#     theft_funds = forms.IntegerField(widget=RadioSelectLikert)
#     alter_reports = forms.IntegerField(widget=RadioSelectLikert)
#     evade_taxes = forms.IntegerField(widget=RadioSelectLikert)
#     private_use_resources = forms.IntegerField(widget=RadioSelectLikert)

#     comments = forms.CharField(
#         widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Other Comments'}),
#         required=False,
#         label="Other Comments"
#     )

#     class Meta:
#         model = CorruptionResponse
#         fields = '__all__'
#         exclude = ['respondent']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Apply INITIAL (Baseline) question wording
#         for field_name, label in INITIAL_CORRUPTION_LABELS.items():
#             if field_name in self.fields:
#                 self.fields[field_name].label = label


# # === 2. POST-INTERVENTION FORM (After Digital Lens) ===
# class PostInterventionCorruptionForm(forms.ModelForm):
#     public_bribes = forms.IntegerField(widget=RadioSelectLikert)
#     request_gifts = forms.IntegerField(widget=RadioSelectLikert)
#     convenience_bribes = forms.IntegerField(widget=RadioSelectLikert)
#     faster_services = forms.IntegerField(widget=RadioSelectLikert)
#     concealment_bribes = forms.IntegerField(widget=RadioSelectLikert)

#     use_facilities_family = forms.IntegerField(widget=RadioSelectLikert)
#     no_public_ads = forms.IntegerField(widget=RadioSelectLikert)
#     same_tribe = forms.IntegerField(widget=RadioSelectLikert)
#     tribe_promotions = forms.IntegerField(widget=RadioSelectLikert)
#     unequal_pay = forms.IntegerField(widget=RadioSelectLikert)
#     unqualified_employ = forms.IntegerField(widget=RadioSelectLikert)

#     low_price_assets = forms.IntegerField(widget=RadioSelectLikert)
#     favor_friends = forms.IntegerField(widget=RadioSelectLikert)
#     no_demote_friends = forms.IntegerField(widget=RadioSelectLikert)
#     political_appoint = forms.IntegerField(widget=RadioSelectLikert)
#     sex_discrimination = forms.IntegerField(widget=RadioSelectLikert)
#     same_religion = forms.IntegerField(widget=RadioSelectLikert)

#     private_work_hours = forms.IntegerField(widget=RadioSelectLikert)
#     theft_properties = forms.IntegerField(widget=RadioSelectLikert)
#     theft_funds = forms.IntegerField(widget=RadioSelectLikert)
#     alter_reports = forms.IntegerField(widget=RadioSelectLikert)
#     evade_taxes = forms.IntegerField(widget=RadioSelectLikert)
#     private_use_resources = forms.IntegerField(widget=RadioSelectLikert)

#     comments = forms.CharField(
#         widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Other Comments'}),
#         required=False,
#         label="Other Comments"
#     )

#     class Meta:
#         model = CorruptionResponse
#         fields = '__all__'
#         exclude = ['respondent']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Apply POST-INTERVENTION wording
#         for field_name, label in POST_CORRUPTION_LABELS.items():
#             if field_name in self.fields:
#                 self.fields[field_name].label = label


# # === 3. KNOWLEDGE / PERCEPTION OF DIGITAL LENS FORM ===
# # Uses SAME wording as Post-intervention
# class KnowledgePerceptionForm(PostInterventionCorruptionForm):
#     """
#     This is the 3rd questionnaire (pages 4–6 in the document)
#     It uses the exact same mitigation wording as Post-intervention
#     """
#     class Meta(PostInterventionCorruptionForm.Meta):
#         pass


# # === SECTION B FORMS (Only used in Baseline) ===
# class EconomicForm(forms.ModelForm):
#     adequate_income = forms.IntegerField(widget=RadioSelectLikert, label="1: Employees in our organization have adequate-income levels")
#     economic_freedom = forms.IntegerField(widget=RadioSelectLikert, label="2: We have economic freedom whereby Individuals control their assets and labour without state interruptions")
#     inflation_affect = forms.IntegerField(widget=RadioSelectLikert, label="3: Employees’ income is affected by inflation")
#     international_trade = forms.IntegerField(widget=RadioSelectLikert, label="4: We freely engage in international trade activities")
#     national_trade = forms.IntegerField(widget=RadioSelectLikert, label="5: We freely engage in national trade activities")

#     class Meta:
#         model = EconomicResponse
#         exclude = ['respondent']


# class SocialForm(forms.ModelForm):
#     social_distress = forms.IntegerField(widget=RadioSelectLikert, label="1: Some workers suffer from social distress")
#     social_exclusion = forms.IntegerField(widget=RadioSelectLikert, label="2: Social exclusion is experienced by some workers")
#     religious_beliefs = forms.IntegerField(widget=RadioSelectLikert, label="3: Employees have strong religious beliefs")
#     male_dominance = forms.IntegerField(widget=RadioSelectLikert, label="4: Majority of males take administrative/management roles compared to females")
#     middle_class_life = forms.IntegerField(widget=RadioSelectLikert, label="5: Most people live a life of middle-income class")
#     value_education = forms.IntegerField(widget=RadioSelectLikert, label="6: Our organisation values highly educated employees")
#     low_job_intensity = forms.IntegerField(widget=RadioSelectLikert, label="7: We have workers from families with low job intensity like families with few people having formal jobs")

#     class Meta:
#         model = SocialResponse
#         exclude = ['respondent']


# class PoliticalForm(forms.ModelForm):
#     rule_of_law = forms.IntegerField(widget=RadioSelectLikert, label="1: Our decisions are based on rule of Law that is individuals are subjected to the same laws")
#     state_land_control = forms.IntegerField(widget=RadioSelectLikert, label="2: In our country, land is controlled by the state")
#     democracy_practice = forms.IntegerField(widget=RadioSelectLikert, label="3: We often practise democracy in our organization")
#     political_rights = forms.IntegerField(widget=RadioSelectLikert, label="4: There is observance of political rights")
#     civil_liberties = forms.IntegerField(widget=RadioSelectLikert, label="5: We have civil liberties that is personal liberties without interference from the state")
#     fair_elections = forms.IntegerField(widget=RadioSelectLikert, label="6: There is freedom to choose leaders via fair elections")
#     political_stability = forms.IntegerField(widget=RadioSelectLikert, label="7: Political stability exists in our organisation")
#     policy_framework = forms.IntegerField(widget=RadioSelectLikert, label="8: We are guided by policy and institutional framework")

#     class Meta:
#         model = PoliticalResponse
#         exclude = ['respondent']


# class DigitalForm(forms.ModelForm):
#     digital_infra_avail = forms.IntegerField(widget=RadioSelectLikert, label="1: There is availability of digital infrastructure")
#     access_computers = forms.IntegerField(widget=RadioSelectLikert, label="2: We have access to digital infrastructure like computers")
#     support_infra = forms.IntegerField(widget=RadioSelectLikert, label="3: We have access to support infrastructure like internet and electricity")
#     invest_policy = forms.IntegerField(widget=RadioSelectLikert, label="4: We have a policy of investing in digital Technology")
#     improves_work = forms.IntegerField(widget=RadioSelectLikert, label="5: The use of digital technology makes work better")
#     frequent_use = forms.IntegerField(widget=RadioSelectLikert, label="6: We frequently use digital technologies for executing activities")

#     class Meta:
#         model = DigitalResponse
#         exclude = ['respondent']


# class ParticipationForm(forms.ModelForm):
#     council_meetings = forms.IntegerField(widget=RadioSelectLikert, label="1: I have attended local council meetings in the past 12 months")
#     discuss_policies = forms.IntegerField(widget=RadioSelectLikert, label="2: I take part in discussion of public policies in the country")
#     contribute_services = forms.IntegerField(widget=RadioSelectLikert, label="3: I contribute and deliberate on services in my country")
#     public_info = forms.IntegerField(widget=RadioSelectLikert, label="4: The government provides me with public information as and when demanded")
#     decision_making = forms.IntegerField(widget=RadioSelectLikert, label="5: I engage in decision making processes of the government")

#     class Meta:
#         model = ParticipationResponse
#         exclude = ['respondent']











# # ——————————————————— Demographics ———————————————————
# class RespondentForm(forms.ModelForm):
#     class Meta:
#         model = Respondent
#         fields = '__all__'
#         widgets = {
#             'gender': forms.RadioSelect,
#             'age': forms.RadioSelect,
#             'education': forms.RadioSelect,
#             'religion': forms.RadioSelect,
#             'experience': forms.RadioSelect,
#             'family_size': forms.RadioSelect,
#             'marital_status': forms.RadioSelect,
#             'income': forms.RadioSelect,
#             'org_age': forms.RadioSelect,
#             'org_size': forms.RadioSelect,
#             'org_location': forms.RadioSelect,
#         }

# # ——————————————————— Section B (Baseline Only) ———————————————————
# class EconomicForm(forms.ModelForm):
#     class Meta:
#         model = EconomicResponse
#         exclude = ['respondent']
#         widgets = {field: RadioSelectLikert for field in EconomicResponse._meta.get_fields() if hasattr(field, 'name') and field.name not in ['id', 'respondent']}

# class SocialForm(forms.ModelForm):
#     class Meta:
#         model = SocialResponse
#         exclude = ['-SocialResponse']
#         widgets = {field: RadioSelectLikert for field in SocialResponse._meta.get_fields() if hasattr(field, 'name') and field.name not in ['id', 'respondent']}

# class PoliticalForm(forms.ModelForm):
#     class Meta:
#         model = PoliticalResponse
#         exclude = ['respondent']

# class DigitalForm(forms.ModelForm):
#     class Meta:
#         model = DigitalResponse
#         exclude = ['respondent']

# class ParticipationForm(forms.ModelForm):
#     class Meta:
#         model = ParticipationResponse
#         exclude = ['respondent']

# # ——————————————————— Corruption Forms ———————————————————
# class BaselineCorruptionForm(forms.ModelForm):
#     comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Other Comments...'}), required=False)

#     class Meta:
#         model = CorruptionResponse
#         exclude = ['respondent']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, label in INITIAL_CORRUPTION_LABELS.items():
#             if field_name in self.fields:
#                 self.fields[field_name].label = label
#                 self.fields[field_name].widget = RadioSelectLikert()

# class MitigationCorruptionForm(forms.ModelForm):
#     comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Other Comments...'}), required=False)

#     class Meta:
#         model = CorruptionResponse
#         exclude = ['respondent']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, label in POST_CORRUPTION_LABELS.items():
#             if field_name in self.fields:
#                 self.fields[field_name].label = label
#                 self.fields[field_name].widget = RadioSelectLikert()

# # Knowledge/Perception uses same form as Post but with modified Digital labels
# class KnowledgeDigitalForm(DigitalForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['digital_infra_avail'].label = "The Corruption Digital Lens ensures availability of transparent digital infrastructure"
#         self.fields['access_computers'].label = "The Corruption Digital Lens provides real-time access to organizational systems (reducing manual interference)"
#         self.fields['support_infra'].label = "The Corruption Digital Lens guarantees reliable support infrastructure (internet, power, audit logs)"
#         self.fields['invest_policy'].label = "The Corruption Digital Lens enforces policy compliance in digital investments and usage"
#         self.fields['improves_work'].label = "The Corruption Digital Lens significantly improves transparency and efficiency in work processes"
#         self.fields['frequent_use'].label = "The Corruption Digital Lens promotes frequent and accountable use of digital systems"













# forms.py
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
