from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages

from .models import CorruptionForm, Act, Comment, CorruptionPage, Interplay, InterplayComment
# from .forms import CommentForm, IncidentForm, FeedbackForm
from django.views import View
from .forms import ( CommentForm, IncidentForm, FeedbackForm)

def home(request):
    objs = CorruptionForm.objects.all()
    corruption = CorruptionPage.objects.first()
    if 'searchq' in request.GET:
        search = request.GET['searchq']
        if search:
            if search == 'corruption':
                objs = objs
            else:
                objs = objs.filter(Q(name__icontains=search))
            return render(request, "home.html",  {"formsc": objs, "search": 1,
                                                  "corruption": corruption})
    return render(request, "home.html",  {"formsc": objs, "search": 0,
                                          "corruption": corruption})

# def act_detail(request, corruption_id):
#     # Fetch item data based on item_id
#     item = {'id': corruption_id, 'name': f'Item {corruption_id}'}
#     return render(request, 'corruption_detail.html', {'item': item})

def register_like(request, act_id, corruption_id):
    if act_id and corruption_id:
        act = Act.objects.get(id=act_id)
        act.likes += 1
        act.save()
        return redirect('act_detail', corruption_id=corruption_id)
    
def interplay_like(request, interplay_id, corruption_id):
    if interplay_id and corruption_id:
        inter = Interplay.objects.get(id=interplay_id)
        inter.likes += 1
        inter.save()
        return redirect('act_detail', corruption_id=corruption_id)


def act_detail(request, corruption_id, *args, **kwargs):
    c_form = CorruptionForm.objects.get(id=corruption_id)
    factors = c_form.factors.all()
    acts = c_form.acts.all()
    interplay = [Interplay.objects.filter(act=act).first() for act in acts if Interplay.objects.filter(act=act).first()]
    context = {'c_form': c_form, "factors": factors, "acts": acts, "form": CommentForm(), 'interplay': interplay}
    if request.method == 'POST':
        inter_id = request.POST.get('interplay_id')
        inter_comment = request.POST.get('interplay_message')
        if inter_id and inter_comment:
            inter = Interplay.objects.get(id=inter_id)
            InterplayComment.objects.create(interplay=inter, comment=inter_comment)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            act = form.cleaned_data.get('act')
            act = act[0] if isinstance(act, list) else act
            act = Act.objects.filter(id=int(act)).first()
            _ = Comment.objects.create(comment=comment, act=act)
            # form.save()
            return redirect('act_detail', corruption_id=corruption_id)
    return render(request, 'corruption_detail.html', context)

def report_incident(request):
    context = {"form": IncidentForm()}
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report-incident')
    return render(request, 'report.html', context)

def feedback(request):
    form = FeedbackForm()
    form.fields.get('name').required = False
    form.fields.get('email').required = False
    context = {"form": form}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Feedback submitted successfuly. Thank you")
            return redirect('feedback')
    return render(request, 'feedback.html', context)

##############################
#
# Questionnaire views
#
###############################
# class SurveyView(View):
#     template_name = 'survey.html'

#     def get(self, request, is_post=False):
#         context = {
#             'respondent_form': RespondentForm(),
#             'economic_form': EconomicForm(),
#             'social_form': SocialForm(),
#             'political_form': PoliticalForm(),
#             'digital_form': DigitalForm(),
#             'participation_form': ParticipationForm(),
#             'corruption_form': CorruptionFormForm(),
#             'is_post': is_post,
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, is_post=False):
#         respondent_form = RespondentForm(request.POST)
#         print(respondent_form.is_valid())
#         forms = [
#             EconomicForm(request.POST),
#             SocialForm(request.POST),
#             PoliticalForm(request.POST),
#             DigitalForm(request.POST),
#             ParticipationForm(request.POST),
#             CorruptionFormForm(request.POST),
#         ]
        
#         for _f in forms:
#             print("===============================================")
#             print("===============================================")
#             print("===============================================")
#             # print(_f.is_valid(), _f.data)
#             import pprint
#             pprint.pprint(_f.data)
#             print("===============================================")
#             print("===============================================")
#             print("===============================================")
        
#         if respondent_form.is_valid() and all(f.is_valid() for f in forms):
#             print("********. Its vallid *********")
#             respondent = respondent_form.save(commit=False)
#             respondent.is_post_intervention = is_post
#             respondent.save()
            
#             for form in forms:
#                 instance = form.save(commit=False)
#                 instance.respondent = respondent
#                 instance.save()
                
            
            
#             return redirect('thank_you')
        
#         # If invalid, re-render with errors
#         context = {
#             'respondent_form': respondent_form,
#             'economic_form': forms[0],
#             'social_form': forms[1],
#             'political_form': forms[2],
#             'digital_form': forms[3],
#             'participation_form': forms[4],
#             'corruption_form': forms[5],
#             'is_post': is_post,
#         }
#         return render(request, self.template_name, context)

# def thank_you(request):
#     return render(request, 'thank_you.html')

# def survey_view(request, is_post=False):
#     # if request.method == 'POST':
#     #     respondent_form = RespondentForm(request.POST)
#     #     # ... save all
#     # else:
#     #     respondent_form = RespondentForm(initial={'is_post_intervention': is_post})
#     #     # instantiate others

#     # context = {
#     #     'is_post': is_post,
#     #     'respondent_form': respondent_form,
#     #     'economic_form': EconomicForm(),
#     #     'social_form': SocialForm(),
#     #     # ... etc
#     #     'corruption_form': CorruptionFormForm(),
#     # }
#     # return render(request, 'survey.html', context)

#     # is_post = (survey_type == 'post')

#     success = False

#     if request.method == 'POST':
#         respondent_form = RespondentForm(request.POST)
#         corruption_form = CorruptionFormForm(request.POST)

#         if respondent_form.is_valid():
#             respondent = respondent_form.save(commit=False)
#             respondent.is_post_intervention = is_post
#             respondent.save()

#             # Attach respondent to corruption form
#             corruption_form = CorruptionFormForm(request.POST, respondent=respondent)
#             if corruption_form.is_valid():
#                 corruption_form.save()
#                 success = True

#                 # Save other sections only for initial survey
#                 if not is_post:
#                     # Example: save economic
#                     economic_form = EconomicForm(request.POST, instance=EconomicResponse(respondent=respondent))
#                     if economic_form.is_valid():
#                         economic_form.save()
#                     # ... repeat for social, political, etc.

#     else:
#         # GET request
#         respondent_form = RespondentForm(initial={'is_post_intervention': is_post})

#         # Create **temporary** respondent for label logic (not saved)
#         temp_respondent = Respondent(is_post_intervention=is_post)
#         corruption_form = CorruptionFormForm(respondent=temp_respondent)

#         # Other forms (only for initial)
#         economic_form = EconomicForm() if not is_post else None
#         social_form = SocialForm() if not is_post else None
#         political_form = PoliticalForm() if not is_post else None
#         digital_form = DigitalForm() if not is_post else None
#         participation_form = ParticipationForm() if not is_post else None

#     context = {
#         'is_post': is_post,
#         'respondent_form': respondent_form,
#         'corruption_form': corruption_form,
#         'success': success,
#     }
#     if not is_post:
#         context.update({
#             'economic_form': economic_form,
#             'social_form': social_form,
#             'political_form': political_form,
#             'digital_form': digital_form,
#             'participation_form': participation_form,
#         })

#     return render(request, 'survey.html', context)



# class SurveyView(View):
#     template_name = 'survey.html'

#     def get(self, request, is_post=False):
#         context = {
#             'respondent_form': RespondentForm(),
#             'corruption_form': CorruptionFormForm(),
#             'is_post': is_post,
#         }
#         if not is_post:
#             context.update({
#                 'economic_form': EconomicForm(),
#                 'social_form': SocialForm(),
#                 'political_form': PoliticalForm(),
#                 'digital_form': DigitalForm(),
#                 'participation_form': ParticipationForm(),
#             })
#         return render(request, self.template_name, context)

#     def post(self, request, is_post=False):
#         respondent_form = RespondentForm(request.POST)
#         corruption_form = CorruptionFormForm(request.POST)
        
#         if not is_post:
#             economic_form = EconomicForm(request.POST)
#             social_form = SocialForm(request.POST)
#             political_form = PoliticalForm(request.POST)
#             digital_form = DigitalForm(request.POST)
#             participation_form = ParticipationForm(request.POST)
#             section_forms = [economic_form, social_form, political_form, digital_form, participation_form]
#         else:
#             section_forms = []
        
#         forms = section_forms + [corruption_form]
        
#         for ff in forms:
#             print(ff.is_valid())
        
#         if respondent_form.is_valid() and all(f.is_valid() for f in forms):
#             respondent = respondent_form.save(commit=False)
#             respondent.is_post_intervention = is_post
#             respondent.save()
            
#             for form in forms:
               
#                 instance = form.save(commit=False)
#                 instance.respondent = respondent
#                 instance.save()
            
#             return redirect('thank_you')
        
#         # If invalid, re-render with errors (and log for debugging)
#         print("Form errors:")  # Add this for debugging in console
#         print(respondent_form.errors)
#         print(corruption_form.errors)
#         for f in section_forms:
#             print(f.errors)
        
#         context = {
#             'respondent_form': respondent_form,
#             'corruption_form': corruption_form,
#             'is_post': is_post,
#         }
#         if not is_post:
#             context.update({
#                 'economic_form': economic_form,
#                 'social_form': social_form,
#                 'political_form': political_form,
#                 'digital_form': digital_form,
#                 'participation_form': participation_form,
#             })
#         return render(request, self.template_name, context)

def thank_you(request):
    return render(request, 'thank_you.html')



# from .models import Respondent
# from .forms import (
#     # Demographics
#     KnowledgeDigitalForm,
#     MitigationCorruptionForm,
#     RespondentForm,
#     # Section B (only for baseline)
#     EconomicForm, SocialForm, PoliticalForm, DigitalForm, ParticipationForm,
#     # Corruption Forms
#     BaselineCorruptionForm, PostInterventionCorruptionForm
# )


# class SurveyView(View):
#     template_name = 'survey.html'

#     SURVEY_CONFIG = {
#         'baseline': {
#             'title': 'Baseline Survey (Pre-Intervention)',
#             'show_section_b': True,
#             'full_section_b': True,
#             'corruption_form': BaselineCorruptionForm,
#             'digital_form_class': DigitalForm,
#         },
#         'post': {
#             'title': 'Post-Intervention Survey (After Digital Lens)',
#             'show_section_b': False,
#             'full_section_b': False,
#             'corruption_form': MitigationCorruptionForm,
#             'digital_form_class': None,
#         },
#         'knowledge': {
#             'title': 'Knowledge & Perception of the Corruption Digital Lens',
#             'show_section_b': True,
#             'full_section_b': False,
#             'corruption_form': MitigationCorruptionForm,
#             'digital_form_class': KnowledgeDigitalForm,
#         }
#     }

#     def get(self, request, survey_type='baseline'):
#         if survey_type not in self.SURVEY_CONFIG:
#             return redirect('survey_start')

#         config = self.SURVEY_CONFIG[survey_type]

#         context = {
#             'survey_type': survey_type,
#             'survey_title': config['title'],
#             'respondent_form': RespondentForm(),
#             'corruption_form': config['corruption_form'](),
#             'show_section_b': config['show_section_b'],
#             'full_section_b': config['full_section_b'],
#         }

#         if config['full_section_b']:
#             context.update({
#                 'economic_form': EconomicForm(),
#                 'social_form': SocialForm(),
#                 'political_form': PoliticalForm(),
#                 'digital_form': DigitalForm(),
#                 'participation_form': ParticipationForm(),
#             })
#         elif config['show_section_b']:
#             context['digital_form'] = config['digital_form_class']()

#         return render(request, self.template_name, context)

#     def post(self, request, survey_type='baseline'):
#         if survey_type not in self.SURVEY_CONFIG:
#             return redirect('survey_start')

#         config = self.SURVEY_CONFIG[survey_type]
#         respondent_form = RespondentForm(request.POST)
#         corruption_form = config['corruption_form'](request.POST)

#         section_b_forms = []
#         digital_form = None

#         if config['full_section_b']:
#             forms = [EconomicForm, SocialForm, PoliticalForm, DigitalForm, ParticipationForm]
#             section_b_forms = [f(request.POST) for f in forms]
#         elif config['show_section_b']:
#             digital_form = config['digital_form_class'](request.POST)

#         all_valid = respondent_form.is_valid() and corruption_form.is_valid()
#         if section_b_forms:
#             all_valid = all_valid and all(f.is_valid() for f in section_b_forms)
#         if digital_form:
#             all_valid = all_valid and digital_form.is_valid()

#         if all_valid:
#             respondent = respondent_form.save(commit=False)
#             respondent.survey_type = survey_type
#             respondent.save()

#             if section_b_forms:
#                 for form in section_b_forms:
#                     obj = form.save(commit=False)
#                     obj.respondent = respondent
#                     obj.save()
#             if digital_form:
#                 obj = digital_form.save(commit=False)
#                 obj.respondent = respondent
#                 obj.save()

#             corruption = corruption_form.save(commit=False)
#             corruption.respondent = respondent
#             corruption.save()

#             messages.success(request, "Thank you! Your response has been recorded.")
#             return redirect('survey_complete')

#         # Re-render with errors
#         context = {**locals(), **{'survey_title': config['title']}}
#         return render(request, self.template_name, context)




# views.py
from django.shortcuts import render, redirect
from .forms import SystemForm, PublicForm, EmployeeForm

def get_full_intro():
    return """
    <p>Digital technology framework is defined as an integrated Information Technology based framework consisting of interacting components that work 
together to realize a set of functions to create a usable product for solving a problem (Mousa et al., 2024). Mitigated corruption is a reduction in 
corruption that is achieved when a set of strategies is applied in public organizations. Corruption includes anything that involves abuse of a person’s or 
organization’s position entrusted to them in the public or private sector for the benefit of a few individuals or organizations to detriment of the well-being 
of other people or organizations (Inuwa & Ononiwa, 2020; Damijan, 2023)</p>
<p>Dear respondent, thank you for participating in this survey. You have been earmarked to possess the required knowledge on corruption and its 
mitigation. The purpose of the study is to develop a digital technology framework for mitigating corruption.  The survey will take 
approximately 10 minutes. Participation in the survey is voluntary, and you can choose to exit at any time. You are therefore requested to 
respond to the questions detailed in this survey and the information provided will be handled with at most privacy and will solely be used for 
academic purposes</p>
    """

def system_survey(request):
    intro = f"{get_full_intro()}<p>Please note that this section enables the researcher to obtain information related to how the designed digital tool (The corruption digital lens) mitigates corruption in public organizations</p>"
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = SystemForm()
    demographic_fields = [form['gender'], form['gender_other'], form['age'], form['education'], form['religion'], form['religion_other'], form['experience'], form['family_size'], form['marital'], form['income'], form['org_category'], form['org_age'], form['org_size'], form['org_location']]
    bribery_fields = [form['bribery_1'], form['bribery_2'], form['bribery_3'], form['bribery_4'], form['bribery_5']]
    nepotism_fields = [form['nepotism_1'], form['nepotism_2'], form['nepotism_3'], form['nepotism_4'], form['nepotism_5'], form['nepotism_6']]
    favoritism_fields = [form['favoritism_1'], form['favoritism_2'], form['favoritism_3'], form['favoritism_4'], form['favoritism_5'], form['favoritism_6']]
    embezzlement_fields = [form['embezzlement_1'], form['embezzlement_2'], form['embezzlement_3'], form['embezzlement_4'], form['embezzlement_5'], form['embezzlement_6']]
    comment_field = form['comment']
    return render(request, 'survey.html', {
        'form': form, 'title': 'System Questionnaire', 'intro': intro,
        'demographic_fields': demographic_fields,
        'bribery_fields': bribery_fields, 'nepotism_fields': nepotism_fields,
        'favoritism_fields': favoritism_fields, 'embezzlement_fields': embezzlement_fields,
        'comment_field': comment_field,
    })

def public_survey(request):
    intro = get_full_intro()
    if request.method == 'POST':
        form = PublicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = PublicForm()
    demographic_fields = [form['gender'], form['gender_other'], form['age'], form['education'], form['religion'], form['religion_other'], form['experience'], form['family_size'], form['marital'], form['income'], form['org_name'], form['org_category'], form['org_age'], form['org_size'], form['org_location']]
    economic_fields = [form['economic_1'], form['economic_2'], form['economic_3'], form['economic_4'], form['economic_5']]
    social_fields = [form['social_1'], form['social_2'], form['social_3'], form['social_4'], form['social_5'], form['social_6'], form['social_7']]
    political_fields = [form['political_1'], form['political_2'], form['political_3'], form['political_4'], form['political_5'], form['political_6'], form['political_7'], form['political_8']]
    digital_fields = [form['digital_1'], form['digital_2'], form['digital_3'], form['digital_4'], form['digital_5'], form['digital_6']]
    civic_fields = [form['civic_1'], form['civic_2'], form['civic_3'], form['civic_4'], form['civic_5']]
    bribery_fields = [form['corruption_bribery_1'], form['corruption_bribery_2'], form['corruption_bribery_3'], form['corruption_bribery_4'], form['corruption_bribery_5']]
    nepotism_fields = [form['corruption_nepotism_1'], form['corruption_nepotism_2'], form['corruption_nepotism_3'], form['corruption_nepotism_4'], form['corruption_nepotism_5'], form['corruption_nepotism_6']]
    favoritism_fields = [form['corruption_favoritism_1'], form['corruption_favoritism_2'], form['corruption_favoritism_3'], form['corruption_favoritism_4'], form['corruption_favoritism_5'], form['corruption_favoritism_6']]
    embezzlement_fields = [form['corruption_embezzlement_1'], form['corruption_embezzlement_2'], form['corruption_embezzlement_3'], form['corruption_embezzlement_4'], form['corruption_embezzlement_5'], form['corruption_embezzlement_6']]
    comment_field = form['comment']
    return render(request, 'survey.html', {
        'form': form, 'title': 'Questionnaire for Public', 'intro': intro,
        'demographic_fields': demographic_fields,
        'economic_fields': economic_fields, 'social_fields': social_fields,
        'political_fields': political_fields, 'digital_fields': digital_fields,
        'civic_fields': civic_fields,
        'bribery_fields': bribery_fields, 'nepotism_fields': nepotism_fields,
        'favoritism_fields': favoritism_fields, 'embezzlement_fields': embezzlement_fields,
        'comment_field': comment_field,
    })

def employee_survey(request):
    intro = get_full_intro()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = EmployeeForm()
    demographic_fields = [form['gender'], form['gender_other'], form['age'], form['education'], form['religion'], form['religion_other'], form['experience'], form['family_size'], form['marital'], form['income'], form['org_name'], form['org_category'], form['org_age'], form['org_size'], form['org_location']]
    economic_fields = [form['economic_1'], form['economic_2'], form['economic_3'], form['economic_4'], form['economic_5']]
    social_fields = [form['social_1'], form['social_2'], form['social_3'], form['social_4'], form['social_5'], form['social_6'], form['social_7']]
    political_fields = [form['political_1'], form['political_2'], form['political_3'], form['political_4'], form['political_5'], form['political_6'], form['political_7'], form['political_8']]
    digital_fields = [form['digital_1'], form['digital_2'], form['digital_3'], form['digital_4'], form['digital_5'], form['digital_6']]
    civic_fields = [form['civic_1'], form['civic_2'], form['civic_3'], form['civic_4'], form['civic_5']]
    bribery_fields = [form['corruption_bribery_1'], form['corruption_bribery_2'], form['corruption_bribery_3'], form['corruption_bribery_4'], form['corruption_bribery_5']]
    nepotism_fields = [form['corruption_nepotism_1'], form['corruption_nepotism_2'], form['corruption_nepotism_3'], form['corruption_nepotism_4'], form['corruption_nepotism_5'], form['corruption_nepotism_6']]
    favoritism_fields = [form['corruption_favoritism_1'], form['corruption_favoritism_2'], form['corruption_favoritism_3'], form['corruption_favoritism_4'], form['corruption_favoritism_5'], form['corruption_favoritism_6']]
    embezzlement_fields = [form['corruption_embezzlement_1'], form['corruption_embezzlement_2'], form['corruption_embezzlement_3'], form['corruption_embezzlement_4'], form['corruption_embezzlement_5'], form['corruption_embezzlement_6']]
    comment_field = form['comment']
    return render(request, 'survey.html', {
        'form': form, 'title': 'Questionnaire for Employees', 'intro': intro,
        'demographic_fields': demographic_fields,
        'economic_fields': economic_fields, 'social_fields': social_fields,
        'political_fields': political_fields, 'digital_fields': digital_fields,
        'civic_fields': civic_fields,
        'bribery_fields': bribery_fields, 'nepotism_fields': nepotism_fields,
        'favoritism_fields': favoritism_fields, 'embezzlement_fields': embezzlement_fields,
        'comment_field': comment_field,
    })

def thanks(request):
    return render(request, 'thank_you.html')