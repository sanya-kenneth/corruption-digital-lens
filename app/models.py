from django.db import models


class CorruptionForm(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = "Corruption forms"

    def __str__(self):
        return self.name


class Factor(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    corruption_form = models.ManyToManyField(CorruptionForm, related_name='factors')
    indicators = models.CharField(max_length=3000, null=True, blank=True)
    references = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Act(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    notes = models.TextField(null=True, blank=True)
    interplay = models.TextField(null=True)
    references = models.TextField(null=True, blank=True)
    corruption_form = models.ManyToManyField(CorruptionForm, related_name='acts')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    act = models.ForeignKey(Act, on_delete=models.CASCADE, related_name='act', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def ___str__(self):
        return f"{self.comment[:15]} {self.created_at}"
    
    class Meta:
        verbose_name = 'Acts comments'
        verbose_name_plural = 'Acts comments'
    

class Incident(models.Model):
    form_of_corruption = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    
class Feedback(models.Model):
    FEEDBACK_CHOICES = [
        (0, "Bug Report"),
        (1, "Feature Request"),
        (2, "General Feedback"),
        (3, "Compliment"),
        (4, "Complaint")
        ]
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    feedback_type = models.SmallIntegerField(choices=FEEDBACK_CHOICES, default=2)
    message = models.TextField()

    def __str__(self):
        _type = "Bug report" if self.feedback_type == 0 else "Feature request" if\
            self.feedback_type == 1 else "General Feedback" if self.feedback_type == 2 else\
                "General Feedback" if self.feedback_type == 2 else "Compliment" if self.feedback_type == 3 else "Complaint"
        return f"{self.name}_{_type}_{self.message[:30]}"
    
    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'


class CorruptionPage(models.Model):
    definition = models.TextField(default="Corruption is receiving, asking for or giving any gratification to induce a person to do a favour with a corrupt intent.")
    notes = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"corruption => {self.definition[:70]}"

    class Meta:
        verbose_name = "Corruption page"
        verbose_name_plural = "Corruption page"
        
        
class Interplay(models.Model):
    name = models.CharField(max_length=150)
    factors = models.CharField(max_length=3000, null=True, blank=True)
    act = models.ForeignKey(Act, on_delete=models.CASCADE, related_name='act_interplay')
    notes = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    # corruption_form = models.ManyToManyField(CorruptionForm, related_name='interplay')
    references = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Interplay"
        

class InterplayComment(models.Model):
    interplay = models.ForeignKey(Interplay, on_delete=models.CASCADE, 
                                  related_name="interplay_comments")
    comment = models.TextField()
    

######################################################
#
# Questionnaire models
#
#######################################################

# class Respondent(models.Model):
#     GENDER_CHOICES = [
#         ('male', 'Male'),
#         ('female', 'Female')
#     ]
#     AGE_CHOICES = [
#         ('18-20', '18-20'),
#         ('21-29', '21-29'),
#         ('30-39', '30-39'),
#         ('40-49', '40-49'),
#         ('50+', '50 and above'),
#     ]
#     EDUCATION_CHOICES = [
#         ('certificate', 'Certificate'),
#         ('diploma', 'Diploma'),
#         ('bachelors', 'Bachelors'),
#         ('pgd_masters', 'PGD/Masters'),
#         ('phd', 'PhD'),
#     ]
#     RELIGION_CHOICES = [
#         ('protestant', 'Protestant'),
#         ('catholic', 'Catholic'),
#         ('islam', 'Islam'),
#         ('pentecostal', 'Pentecostal'),
#         ('other', 'Other'),
#     ]
#     EXPERIENCE_CHOICES = [
#         ('<1', '<1'),
#         ('1-4', '1-4'),
#         ('5-9', '5-9'),
#         ('10+', '10+ years'),
#     ]
#     FAMILY_SIZE_CHOICES = [
#         ('1-3', '1-3'),
#         ('4-6', '4-6'),
#         ('7-9', '7-9'),
#         ('10+', '10+'),
#     ]
#     MARITAL_CHOICES = [
#         ('married', 'Married'),
#         ('single', 'Single'),
#         ('divorced', 'Divorced'),
#         ('re_married', 'Re-married'),
#         ('cohabiting', 'Cohabiting'),
#     ]
#     INCOME_CHOICES = [
#         ('1-2', '1-2 Million UGX'),
#         ('3-5', '3-5 Million UGX'),
#         ('6-9', '6-9 Million UGX'),
#         ('10+', '10+ Million UGX'),
#     ]
#     ORG_AGE_CHOICES = [
#         ('0-4', '0-4'),
#         ('5-9', '5-9'),
#         ('10-14', '10-14'),
#         ('15-19', '15-19'),
#         ('20+', '20+'),
#     ]
#     ORG_SIZE_CHOICES = [
#         ('<10', '<10'),
#         ('10-49', '10-49'),
#         ('50-99', '50-99'),
#         ('100+', '100+'),
#     ]
#     ORG_LOCATION_CHOICES = [
#         ('northern', 'Northern'),
#         ('western', 'Western'),
#         ('eastern', 'Eastern'),
#         ('central', 'Central'),
#     ]
    
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     age = models.CharField(max_length=10, choices=AGE_CHOICES)
#     education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
#     religion = models.CharField(max_length=20, choices=RELIGION_CHOICES)
#     religion_other = models.CharField(max_length=100, blank=True)
#     experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
#     family_size = models.CharField(max_length=10, choices=FAMILY_SIZE_CHOICES)
#     marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
#     income = models.CharField(max_length=10, choices=INCOME_CHOICES)
#     org_category = models.CharField(max_length=200)
#     org_age = models.CharField(max_length=10, choices=ORG_AGE_CHOICES)
#     org_size = models.CharField(max_length=10, choices=ORG_SIZE_CHOICES)
#     org_location = models.CharField(max_length=20, choices=ORG_LOCATION_CHOICES)
    
#     is_post_intervention = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

# LIKERT_CHOICES = [
#     (1, 'Strongly Disagree'),
#     (2, 'Disagree'),
#     (3, 'Somewhat Agree'),
#     (4, 'Agree'),
#     (5, 'Strongly Agree'),
# ]

# class EconomicResponse(models.Model):
#     respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
#     adequate_income = models.IntegerField(choices=LIKERT_CHOICES)
#     economic_freedom = models.IntegerField(choices=LIKERT_CHOICES)
#     inflation_affect = models.IntegerField(choices=LIKERT_CHOICES)
#     international_trade = models.IntegerField(choices=LIKERT_CHOICES)
#     national_trade = models.IntegerField(choices=LIKERT_CHOICES)

# class SocialResponse(models.Model):
#     respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
#     social_distress = models.IntegerField(choices=LIKERT_CHOICES)
#     social_exclusion = models.IntegerField(choices=LIKERT_CHOICES)
#     religious_beliefs = models.IntegerField(choices=LIKERT_CHOICES)
#     male_dominance = models.IntegerField(choices=LIKERT_CHOICES)
#     middle_class_life = models.IntegerField(choices=LIKERT_CHOICES)
#     value_education = models.IntegerField(choices=LIKERT_CHOICES)
#     low_job_intensity = models.IntegerField(choices=LIKERT_CHOICES)

# class PoliticalResponse(models.Model):
#     respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
#     rule_of_law = models.IntegerField(choices=LIKERT_CHOICES)
#     state_land_control = models.IntegerField(choices=LIKERT_CHOICES)
#     democracy_practice = models.IntegerField(choices=LIKERT_CHOICES)
#     political_rights = models.IntegerField(choices=LIKERT_CHOICES)
#     civil_liberties = models.IntegerField(choices=LIKERT_CHOICES)
#     fair_elections = models.IntegerField(choices=LIKERT_CHOICES)
#     political_stability = models.IntegerField(choices=LIKERT_CHOICES)
#     policy_framework = models.IntegerField(choices=LIKERT_CHOICES)

# class DigitalResponse(models.Model):
#     respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
#     digital_infra_avail = models.IntegerField(choices=LIKERT_CHOICES)
#     access_computers = models.IntegerField(choices=LIKERT_CHOICES)
#     support_infra = models.IntegerField(choices=LIKERT_CHOICES)
#     invest_policy = models.IntegerField(choices=LIKERT_CHOICES)
#     improves_work = models.IntegerField(choices=LIKERT_CHOICES)
#     frequent_use = models.IntegerField(choices=LIKERT_CHOICES)

# class ParticipationResponse(models.Model):
#     respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
#     council_meetings = models.IntegerField(choices=LIKERT_CHOICES)
#     discuss_policies = models.IntegerField(choices=LIKERT_CHOICES)
#     contribute_services = models.IntegerField(choices=LIKERT_CHOICES)
#     public_info = models.IntegerField(choices=LIKERT_CHOICES)
#     decision_making = models.IntegerField(choices=LIKERT_CHOICES)

# class CorruptionResponse(models.Model):
#     respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
#     # Bribery
#     public_bribes = models.IntegerField(choices=LIKERT_CHOICES)
#     request_gifts = models.IntegerField(choices=LIKERT_CHOICES)
#     convenience_bribes = models.IntegerField(choices=LIKERT_CHOICES)
#     faster_services = models.IntegerField(choices=LIKERT_CHOICES)
#     concealment_bribes = models.IntegerField(choices=LIKERT_CHOICES)
#     # Nepotism
#     use_facilities_family = models.IntegerField(choices=LIKERT_CHOICES)
#     no_public_ads = models.IntegerField(choices=LIKERT_CHOICES)
#     same_tribe = models.IntegerField(choices=LIKERT_CHOICES)
#     tribe_promotions = models.IntegerField(choices=LIKERT_CHOICES)
#     unequal_pay = models.IntegerField(choices=LIKERT_CHOICES)
#     unqualified_employ = models.IntegerField(choices=LIKERT_CHOICES)
#     # Favoritism
#     low_price_assets = models.IntegerField(choices=LIKERT_CHOICES)
#     favor_friends = models.IntegerField(choices=LIKERT_CHOICES)
#     no_demote_friends = models.IntegerField(choices=LIKERT_CHOICES)
#     political_appoint = models.IntegerField(choices=LIKERT_CHOICES)
#     sex_discrimination = models.IntegerField(choices=LIKERT_CHOICES)
#     same_religion = models.IntegerField(choices=LIKERT_CHOICES)
#     # Embezzlement
#     private_work_hours = models.IntegerField(choices=LIKERT_CHOICES)
#     theft_properties = models.IntegerField(choices=LIKERT_CHOICES)
#     theft_funds = models.IntegerField(choices=LIKERT_CHOICES)
#     alter_reports = models.IntegerField(choices=LIKERT_CHOICES)
#     evade_taxes = models.IntegerField(choices=LIKERT_CHOICES)
#     private_use_resources = models.IntegerField(choices=LIKERT_CHOICES)
    
#     comments = models.TextField(blank=True)


# class Respondent(models.Model):
#     # --- Demographics ---
#     GENDER_CHOICES = [
#         ('male', 'Male'),
#         ('female', 'Female')
#     ]
#     AGE_CHOICES = [
#         ('18-20', '18-20'),
#         ('21-29', '21-29'),
#         ('30-39', '30-39'),
#         ('40-49', '40-49'),
#         ('50+', '50 and above'),
#     ]
#     EDUCATION_CHOICES = [
#         ('certificate', 'Certificate'),
#         ('diploma', 'Diploma'),
#         ('bachelors', 'Bachelors'),
#         ('pgd_masters', 'PGD/Masters'),
#         ('phd', 'PhD'),
#     ]
#     RELIGION_CHOICES = [
#         ('protestant', 'Protestant'),
#         ('catholic', 'Catholic'),
#         ('islam', 'Islam'),
#         ('pentecostal', 'Pentecostal'),
#         ('other', 'Other'),
#     ]
#     EXPERIENCE_CHOICES = [
#         ('<1', '<1'),
#         ('1-4', '1-4'),
#         ('5-9', '5-9'),
#         ('10+', '10+ years'),
#     ]
#     FAMILY_SIZE_CHOICES = [
#         ('1-3', '1-3'),
#         ('4-6', '4-6'),
#         ('7-9', '7-9'),
#         ('10+', '10+'),
#     ]
#     MARITAL_CHOICES = [
#         ('married', 'Married'),
#         ('single', 'Single'),
#         ('divorced', 'Divorced'),
#         ('re_married', 'Re-married'),
#         ('cohabiting', 'Cohabiting'),
#     ]
#     INCOME_CHOICES = [
#         ('1-2', '1-2 Million UGX'),
#         ('3-5', '3-5 Million UGX'),
#         ('6-9', '6-9 Million UGX'),
#         ('10+', '10+ Million UGX'),
#     ]
#     ORG_AGE_CHOICES = [
#         ('0-4', '0-4'),
#         ('5-9', '5-9'),
#         ('10-14', '10-14'),
#         ('15-19', '15-19'),
#         ('20+', '20+'),
#     ]
#     ORG_SIZE_CHOICES = [
#         ('<10', '<10'),
#         ('10-49', '10-49'),
#         ('50-99', '50-99'),
#         ('100+', '100+'),
#     ]
#     ORG_LOCATION_CHOICES = [
#         ('northern', 'Northern'),
#         ('western', 'Western'),
#         ('eastern', 'Eastern'),
#         ('central', 'Central'),
#     ]
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="1. Gender")

#     # AGE_CHOICES = [('18-20', '18-20'), ('21-29', '21-29'), ('30-39', '30-39'),
#     #                ('40-49', '40-49'), ('50+', '50 and above')]
#     age = models.CharField(max_length=10, choices=AGE_CHOICES, verbose_name="2. Age")

#     # EDUCATION_CHOICES = [('certificate', 'Certificate'), ('diploma', 'Diploma'),
#     #                      ('bachelors', 'Bachelors'), ('pgd_masters', 'PGD/Masters'), ('phd', 'PhD')]
#     education = models.CharField(max_length=20, choices=EDUCATION_CHOICES, verbose_name="3. Highest level of Formal education")

#     # RELIGION_CHOICES = [('protestant', 'Protestant'), ('catholic', 'Catholic'),
#     #                     ('islam', 'Islam'), ('pentecostal', 'Pentecostal'), ('other', 'Other(specify)')]
#     religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, verbose_name="5. Religious Affiliation")
#     religion_other = models.CharField(max_length=100, blank=True, verbose_name="Other (specify)")

#     experience = models.CharField(max_length=10, choices=[('1', '<1'), ('1-4', '1-4'), ('5-9', '5-9'), ('10+', '10+')],
#                                   verbose_name="6. Experience with work in the organization")
#     family_size = models.CharField(max_length=10, choices=[('1-3', '1-3'), ('4-6', '4-6'), ('7-9', '7-9'), ('10+', '10+')],
#                                    verbose_name="7. Family Size (Number of family members)")
#     marital_status = models.CharField(max_length=20,
#                                       choices=[('married', 'Married'), ('single', 'Single'),
#                                                ('divorced', 'Divorced'), ('cohabiting', 'Cohabiting')],
#                                       verbose_name="8. Marital status")
#     income = models.CharField(max_length=10,
#                               choices=[('1.2', '1.2'), ('3.5', '3.5'), ('6-9', '6-9'), ('10+', '10+')],
#                               verbose_name="9. Income category (monthly gross salary in Millions of UGX)")

#     org_category = models.CharField(max_length=100, verbose_name="10. Organization Category")
#     org_age = models.CharField(max_length=10,
#                                choices=[('0-4', '0-4'), ('5-9', '5-9'), ('10-14', '10-14'), ('15-19', '15-19'), ('20+', '20+')],
#                                verbose_name="11. Organization age (in years)")
#     org_size = models.CharField(max_length=10,
#                                 choices=[('<10', '<10'), ('10-49', '10-49'), ('50-99', '50-99'), ('100+', '100+')],
#                                 verbose_name="12. Organization size (No of employees)")
#     org_location = models.CharField(max_length=20,
#                                     choices=[('northern', 'Northern'), ('western', 'Western'),
#                                              ('eastern', 'Eastern'), ('central', 'Central')],
#                                     verbose_name="13. Organization Location")

#     is_post_intervention = models.BooleanField(default=False, verbose_name="Post-Intervention Survey")
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = "Respondent"

# # ----------------------------------------------------------------------
# # Section models – verbose_name = full question text from PDF
# class EconomicResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)

#     adequate_income = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="1: Employees in our organization have adequate-income levels")
#     economic_freedom = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="2: We have economic freedom whereby Individuals control their assets and labour without state interruptions")
#     inflation_affect = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="3: Employees’ income is affected by inflation")
#     international_trade = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="4: We freely engage in international trade activities")
#     national_trade = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="5: We freely engage in national trade activities")

#     class Meta:
#         verbose_name = "Economic Response"


# # --- SocialResponse ---
# class SocialResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     social_distress = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="1: Some workers suffer from social distress")
#     social_exclusion = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="2: Social exclusion is experienced by some workers")
#     religious_beliefs = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="3: Employees have strong religious beliefs")
#     male_dominance = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="4: Majority of males take administrative/management roles compared to females")
#     middle_class_life = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="5: Most people live a life of middle-income class")
#     value_education = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="6: Our organisation values highly educated employees")
#     low_job_intensity = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="7: We have workers from families with low job intensity like families with few people having formal jobs")

# # --- PoliticalResponse ---
# class PoliticalResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     rule_of_law = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="1: Our decisions are based on rule of Law that is individuals are subjected to the same laws")
#     state_land_control = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="2: In our country, land is controlled by the state")
#     democracy_practice = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="3: We often practise democracy in our organization")
#     political_rights = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="4: There is observance of political rights")
#     civil_liberties = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="5: We have civil liberties that is personal liberties without interference from the state")
#     fair_elections = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="6: There is freedom to choose leaders via fair elections")
#     political_stability = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="7: Political stability exists in our organisation")
#     policy_framework = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="8: We are guided by policy and institutional framework")

# # --- DigitalResponse ---
# class DigitalResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     digital_infra_avail = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="1: There is availability of digital infrastructure")
#     access_computers = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="2: We have access to digital infrastructure like computers")
#     support_infra = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="3: We have access to support infrastructure like internet and electricity")
#     invest_policy = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="4: We have a policy of investing in digital Technology")
#     improves_work = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="5: The use of digital technology makes work better")
#     frequent_use = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="6: We frequently use digital technologies for executing activities")

# # --- ParticipationResponse ---
# class ParticipationResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     council_meetings = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="1: I have attended local council meetings in the past 12months")
#     discuss_policies = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="2: I take part in discussion of public policies in the country")
#     contribute_services = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="3: I contribute and deliberate on services in my country")
#     public_info = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="4: The government provides me with public information as and when demanded")
#     decision_making = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="5: I engage in decision making processes of the government")

# # --- CorruptionResponse (initial + post wording) ---
# class CorruptionResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     comments = models.TextField(blank=True, verbose_name="Other Comments")

#     # Bribery
#     public_bribes = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="1: We have people from the public who offer bribes to organization workers")
#     request_gifts = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="2: Organization workers often request for gifts or informal payments to get things done")
#     convenience_bribes = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="3: In our organisation, there are people who usually offer bribes for convenience reasons")
#     faster_services = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="4: People usually offer bribes to get faster services in our organisation")
#     concealment_bribes = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="5: In our organisation, some people offer bribes for concealment of offences committed")

#     # Nepotism
#     use_facilities_family = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="1: Organization officials use facilities like vehicles to benefit their families")
#     no_public_ads = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="2: Job offers are usually not done through public job advertisements in this organisation")
#     same_tribe = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="3: Most people in our organisation come from the same tribe")
#     tribe_promotions = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="4: Promotions of organization workers from the same tribe takes place")
#     unequal_pay = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="5: Some workers earn far more than their colleagues who are of the same rank")
#     unqualified_employ = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="6: At times our organisation employs people without the required academic qualifications")

#     # Favoritism
#     low_price_assets = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="1: There is asset disposition at low prices to friends of organization workers")
#     favor_friends = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="2: Favouring friends and acquaintances over others in profitable activities often takes place")
#     no_demote_friends = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="3: High level managers do not demote or fire friends if they prove to be inefficient")
#     political_appoint = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="4: Appointment and promotion are connected to political affiliation")
#     sex_discrimination = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="5: Sex discrimination at times exists in the recruitment process")
#     same_religion = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="6: Most employees in our organization have the same religious affiliation")

#     # Embezzlement
#     private_work_hours = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="1: Some people do private work during working hours for their personal gain")
#     theft_properties = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="2: There is theft of organizational properties")
#     theft_funds = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="3: There is theft of funds in our organization")
#     alter_reports = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="4: Some accounting officers change figures in financial account reports for their personal gain")
#     evade_taxes = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="5: Some accounting officers sometimes alter financial figures to avoid or evade taxes")
#     private_use_resources = models.IntegerField(choices=LIKERT_CHOICES,
#         verbose_name="6: Agency resources are often used for private purposes")


# LIKERT_CHOICES = [
#     (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Somewhat Agree'),
#     (4, 'Agree'), (5, 'Strongly Agree')
# ]

# # ----------------------------------------------------------------------
# # DEMOGRAPHICS (shared by both surveys)
# # ----------------------------------------------------------------------
# class Respondent(models.Model):
#     # 1. Gender
#     GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="1. Gender")

#     # 2. Age
#     AGE_CHOICES = [('18-20', '18-20'), ('21-29', '21-29'), ('30-39', '30-39'),
#                    ('40-49', '40-49'), ('50+', '50 and above')]
#     age = models.CharField(max_length=10, choices=AGE_CHOICES, verbose_name="2. Age")

#     # 3. Education
#     EDUCATION_CHOICES = [('certificate', 'Certificate'), ('diploma', 'Diploma'),
#                          ('bachelors', 'Bachelors'), ('pgd_masters', 'PGD/Masters'), ('phd', 'PhD')]
#     education = models.CharField(max_length=20, choices=EDUCATION_CHOICES,
#                                  verbose_name="3. Highest level of Formal education")

#     # 5. Religion
#     RELIGION_CHOICES = [('protestant', 'Protestant'), ('catholic', 'Catholic'),
#                         ('islam', 'Islam'), ('pentecostal', 'Pentecostal'), ('other', 'Other(specify)')]
#     religion = models.CharField(max_length=20, choices=RELIGION_CHOICES,
#                                 verbose_name="5. Religious Affiliation")
#     religion_other = models.CharField(max_length=100, blank=True, verbose_name="Other (specify)")

#     # 6. Experience
#     experience = models.CharField(
#         max_length=10,
#         choices=[('1', '<1'), ('1-4', '1-4'), ('5-9', '5-9'), ('10+', '10+')],
#         verbose_name="6. Experience with work in the organization (years)")

#     # 7. Family size
#     family_size = models.CharField(
#         max_length=10,
#         choices=[('1-3', '1-3'), ('4-6', '4-6'), ('7-9', '7-9'), ('10+', '10+')],
#         verbose_name="7. Family Size (Number of family members)")

#     # 8. Marital status
#     marital_status = models.CharField(
#         max_length=20,
#         choices=[('married', 'Married'), ('single', 'Single'),
#                  ('divorced', 'Divorced'), ('cohabiting', 'Cohabiting')],
#         verbose_name="8. Marital status")

#     # 9. Income
#     income = models.CharField(
#         max_length=10,
#         choices=[('1.2', '1.2'), ('3.5', '3.5'), ('6-9', '6-9'), ('10+', '10+')],
#         verbose_name="9. Income category (monthly gross salary in Millions of UGX)")

#     # 10. Org category
#     org_category = models.CharField(max_length=100,
#         verbose_name="10. Organization Category (eg Education, security, Judiciary etc)")

#     # 11. Org age
#     org_age = models.CharField(
#         max_length=10,
#         choices=[('0-4', '0-4'), ('5-9', '5-9'), ('10-14', '10-14'),
#                  ('15-19', '15-19'), ('20+', '20+')],
#         verbose_name="11. Organization age (in years)")

#     # 12. Org size
#     org_size = models.CharField(
#         max_length=10,
#         choices=[('<10', '<10'), ('10-49', '10-49'), ('50-99', '50-99'), ('100+', '100+')],
#         verbose_name="12. Organization size (No of employees)")

#     # 13. Org location
#     org_location = models.CharField(
#         max_length=20,
#         choices=[('northern', 'Northern'), ('western', 'Western'),
#                  ('eastern', 'Eastern'), ('central', 'Central')],
#         verbose_name="13. Organization Location")

#     # ------------------------------------------------------------------
#     # SURVEY TYPE
#     # ------------------------------------------------------------------
#     is_post_intervention = models.BooleanField(
#         default=False,
#         verbose_name="Post-Intervention Survey"
#     )
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = "Respondent"

#     def __str__(self):
#         return f"{self.get_gender_display()} – {self.org_category}"


# # ----------------------------------------------------------------------
# # RESPONSE MODELS – ONE PER SECTION (shared by both surveys)
# # ----------------------------------------------------------------------
# class EconomicResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     adequate_income = models.IntegerField(choices=LIKERT_CHOICES)
#     economic_freedom = models.IntegerField(choices=LIKERT_CHOICES)
#     inflation_affect = models.IntegerField(choices=LIKERT_CHOICES)
#     international_trade = models.IntegerField(choices=LIKERT_CHOICES)
#     national_trade = models.IntegerField(choices=LIKERT_CHOICES)

# class SocialResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     social_distress = models.IntegerField(choices=LIKERT_CHOICES)
#     social_exclusion = models.IntegerField(choices=LIKERT_CHOICES)
#     religious_beliefs = models.IntegerField(choices=LIKERT_CHOICES)
#     male_dominance = models.IntegerField(choices=LIKERT_CHOICES)
#     middle_class_life = models.IntegerField(choices=LIKERT_CHOICES)
#     value_education = models.IntegerField(choices=LIKERT_CHOICES)
#     low_job_intensity = models.IntegerField(choices=LIKERT_CHOICES)

# class PoliticalResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     rule_of_law = models.IntegerField(choices=LIKERT_CHOICES)
#     state_land_control = models.IntegerField(choices=LIKERT_CHOICES)
#     democracy_practice = models.IntegerField(choices=LIKERT_CHOICES)
#     political_rights = models.IntegerField(choices=LIKERT_CHOICES)
#     civil_liberties = models.IntegerField(choices=LIKERT_CHOICES)
#     fair_elections = models.IntegerField(choices=LIKERT_CHOICES)
#     political_stability = models.IntegerField(choices=LIKERT_CHOICES)
#     policy_framework = models.IntegerField(choices=LIKERT_CHOICES)

# class DigitalResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     digital_infra_avail = models.IntegerField(choices=LIKERT_CHOICES)
#     access_computers = models.IntegerField(choices=LIKERT_CHOICES)
#     support_infra = models.IntegerField(choices=LIKERT_CHOICES)
#     invest_policy = models.IntegerField(choices=LIKERT_CHOICES)
#     improves_work = models.IntegerField(choices=LIKERT_CHOICES)
#     frequent_use = models.IntegerField(choices=LIKERT_CHOICES)

# class ParticipationResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     council_meetings = models.IntegerField(choices=LIKERT_CHOICES)
#     discuss_policies = models.IntegerField(choices=LIKERT_CHOICES)
#     contribute_services = models.IntegerField(choices=LIKERT_CHOICES)
#     public_info = models.IntegerField(choices=LIKERT_CHOICES)
#     decision_making = models.IntegerField(choices=LIKERT_CHOICES)

# # ----------------------------------------------------------------------
# # CORRUPTION – DYNAMIC LABELS
# # ----------------------------------------------------------------------
# INITIAL_CORRUPTION_LABELS = {
#     # Bribery
#     'public_bribes': "1: We have people from the public who offer bribes to organization workers",
#     'request_gifts': "2: Organization workers often request for gifts or informal payments to get things done",
#     'convenience_bribes': "3: In our organisation, there are people who usually offer bribes for convenience reasons",
#     'faster_services': "4: People usually offer bribes to get faster services in our organisation",
#     'concealment_bribes': "5: In our organisation, some people offer bribes for concealment of offences committed",

#     # Nepotism
#     'use_facilities_family': "1: Organization officials use facilities like vehicles to benefit their families",
#     'no_public_ads': "2: Job offers are usually not done through public job advertisements in this organisation",
#     'same_tribe': "3: Most people in our organisation come from the same tribe",
#     'tribe_promotions': "4: Promotions of organization workers from the same tribe takes place",
#     'unequal_pay': "5: Some workers earn far more than their colleagues who are of the same rank",
#     'unqualified_employ': "6: At times our organisation employs people without the required academic qualifications",

#     # Favoritism
#     'low_price_assets': "1: There is asset disposition at low prices to friends of organization workers",
#     'favor_friends': "2: Favouring friends and acquaintances over others in profitable activities often takes place",
#     'no_demote_friends': "3: High level managers do not demote or fire friends if they prove to be inefficient",
#     'political_appoint': "4: Appointment and promotion are connected to political affiliation",
#     'sex_discrimination': "5: Sex discrimination at times exists in the recruitment process",
#     'same_religion': "6: Most employees in our organization have the same religious affiliation",

#     # Embezzlement
#     'private_work_hours': "1: Some people do private work during working hours for their personal gain",
#     'theft_properties': "2: There is theft of organizational properties",
#     'theft_funds': "3: There is theft of funds in our organization",
#     'alter_reports': "4: Some accounting officers change figures in financial account reports for their personal gain",
#     'evade_taxes': "5: Some accounting officers sometimes alter financial figures to avoid or evade taxes",
#     'private_use_resources': "6: Agency resources are often used for private purposes",
# }

# POST_CORRUPTION_LABELS = {
#     # Bribery
#     'public_bribes': "1: The corruption digital lens (system) can mitigate bribes offered by the public to organization workers",
#     'request_gifts': "2: The corruption digital lens minimises the request for gifts or informal payments by organization workers from the public to get things done",
#     'convenience_bribes': "3: The corruption digital lens can discourage people who usually offer bribes for convenience reasons",
#     'faster_services': "4: The corruption digital lens can minimise the rate at which people usually offer bribes to get faster services",
#     'concealment_bribes': "5: The corruption digital lens can discourage people who usually offer bribes for concealment of offences committed",

#     # Nepotism
#     'use_facilities_family': "1: The corruption digital lens can discourage organization officials from using facilities like vehicles to benefit their families",
#     'no_public_ads': "2: The corruption digital lens discourages job offers that are not done through public job advertisements",
#     'same_tribe': "3: The corruption digital lens discourages leaders from employing people from only one tribe in the same organization",
#     'tribe_promotions': "4: The corruption digital lens mitigates against promotions of organization workers from the same tribe",
#     'unequal_pay': "5: The corruption digital lens discourages against workers earning far more than their colleagues who are of the same rank",
#     'unqualified_employ': "6: The corruption digital lens exposes employees without the required academic qualifications",

#     # Favoritism
#     'low_price_assets': "1: The corruption digital lens mitigates against asset disposition at low prices to friends of organization workers",
#     'favor_friends': "2: The corruption digital lens discourages against favouring friends and acquaintances over others in profitable activities for example contracts, promotions",
#     'no_demote_friends': "3: The corruption digital lens encourages high level managers to demote or fire friends if they prove to be inefficient",
#     'political_appoint': "4: The corruption digital lens mitigates appointment and promotion based on political affiliation",
#     'sex_discrimination': "5: The corruption digital lens discourages sex discrimination in the recruitment and advancement process of an organization",
#     'same_religion': "6: The corruption digital lens discourages most employees in an organization having the same religious affiliation",

#     # Embezzlement
#     'private_work_hours': "1: The corruption digital lens mitigates people doing private work during working hours for their personal gain",
#     'theft_properties': "2: The corruption digital lens discourages theft of organizational properties",
#     'theft_funds': "3: The corruption digital lens mitigates theft of funds",
#     'alter_reports': "4: The corruption digital lens limits accounting officers from changing figures in financial account reports for their personal gain",
#     'evade_taxes': "5: The corruption digital lens discourages accounting officers from altering financial figures to avoid or evade taxes",
#     'private_use_resources': "6: The corruption digital lens discourages use of agency resources for private purposes",
# }

# class CorruptionResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     comments = models.TextField(blank=True, verbose_name="Other Comments")

#     # Bribery
#     public_bribes = models.IntegerField(choices=LIKERT_CHOICES)
#     request_gifts = models.IntegerField(choices=LIKERT_CHOICES)
#     convenience_bribes = models.IntegerField(choices=LIKERT_CHOICES)
#     faster_services = models.IntegerField(choices=LIKERT_CHOICES)
#     concealment_bribes = models.IntegerField(choices=LIKERT_CHOICES)

#     # Nepotism
#     use_facilities_family = models.IntegerField(choices=LIKERT_CHOICES)
#     no_public_ads = models.IntegerField(choices=LIKERT_CHOICES)
#     same_tribe = models.IntegerField(choices=LIKERT_CHOICES)
#     tribe_promotions = models.IntegerField(choices=LIKERT_CHOICES)
#     unequal_pay = models.IntegerField(choices=LIKERT_CHOICES)
#     unqualified_employ = models.IntegerField(choices=LIKERT_CHOICES)

#     # Favoritism
#     low_price_assets = models.IntegerField(choices=LIKERT_CHOICES)
#     favor_friends = models.IntegerField(choices=LIKERT_CHOICES)
#     no_demote_friends = models.IntegerField(choices=LIKERT_CHOICES)
#     political_appoint = models.IntegerField(choices=LIKERT_CHOICES)
#     sex_discrimination = models.IntegerField(choices=LIKERT_CHOICES)
#     same_religion = models.IntegerField(choices=LIKERT_CHOICES)

#     # Embezzlement
#     private_work_hours = models.IntegerField(choices=LIKERT_CHOICES)
#     theft_properties = models.IntegerField(choices=LIKERT_CHOICES)
#     theft_funds = models.IntegerField(choices=LIKERT_CHOICES)
#     alter_reports = models.IntegerField(choices=LIKERT_CHOICES)
#     evade_taxes = models.IntegerField(choices=LIKERT_CHOICES)
#     private_use_resources = models.IntegerField(choices=LIKERT_CHOICES)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         print(self.__dict__)
#         if self.id:
#             labels = POST_CORRUPTION_LABELS if self.respondent and self.respondent.is_post_intervention else INITIAL_CORRUPTION_LABELS
#             for field_name, label in labels.items():
#                 field = self._meta.get_field(field_name)
#                 field.verbose_name = label



# ################################################
# #
# # WOrking Draft 01
# #
# ################################################



# LIKERT_CHOICES = [
#     (1, 'Strongly Disagree'),
#     (2, 'Disagree'),
#     (3, 'Somewhat Agree'),
#     (4, 'Agree'),
#     (5, 'Strongly Agree'),
# ]

# INITIAL_CORRUPTION_LABELS = {
#     # Bribery (PDF page 3)
#     'public_bribes': 'We have people from the public who offer bribes to organization workers',
#     'request_gifts': 'Organization workers often request for gifts or informal payments to get things done',
#     'convenience_bribes': 'In our organisation, there are people who usually offer bribes for convenience reasons',
#     'faster_services': 'People usually offer bribes to get faster services in our organisation',
#     'concealment_bribes': 'In our organisation, some people offer bribes for concealment of offences committed',

#     # Nepotism (PDF page 3)
#     'use_facilities_family': 'Organization officials use facilities like vehicles to benefit their families',
#     'no_public_ads': 'Job offers are usually not done through public job advertisements in this organisation',
#     'same_tribe': 'Most people in our organisation come from the same tribe',
#     'tribe_promotions': 'Promotions of organization workers from the same tribe takes place',
#     'unequal_pay': 'Some workers earn far more than their colleagues who are of the same rank',
#     'unqualified_employ': 'At times our organisation employs people without the required academic qualifications',

#     # Favoritism (PDF page 3)
#     'low_price_assets': 'There is asset disposition at low prices to friends of organization workers',
#     'favor_friends': 'Favouring friends and acquaintances over others in profitable activities often takes place',
#     'no_demote_friends': 'High level managers do not demote or fire friends if they prove to be inefficient',
#     'political_appoint': 'Appointment and promotion are connected to political affiliation',
#     'sex_discrimination': 'Sex discrimination at times exists in the recruitment process',
#     'same_religion': 'Most employees in our organization have the same religious affiliation',

#     # Embezzlement (PDF page 3-4)
#     'private_work_hours': 'Some people do private work during working hours for their personal gain',
#     'theft_properties': 'There is theft of organizational properties',
#     'theft_funds': 'There is theft of funds in our organization',
#     'alter_reports': 'Some accounting officers change figures in financial account reports for their personal gain',
#     'evade_taxes': 'Some accounting officers sometimes alter financial figures to avoid or evade taxes',
#     'private_use_resources': 'Agency resources are often used for private purposes',
# }

# POST_CORRUPTION_LABELS = {
#     # Bribery (PDF page 5)
#     'public_bribes': 'The corruption digital lens (system) can mitigate bribes offered by the public to organization workers',
#     'request_gifts': 'The corruption digital lens minimises the request for gifts or informal payments by organization workers from the public to get things done',
#     'convenience_bribes': 'The corruption digital lens can discourage people who usually offer bribes for convenience reasons',
#     'faster_services': 'The corruption digital lens can minimise the rate at which people usually offer bribes to get faster services',
#     'concealment_bribes': 'The corruption digital lens can discourage people who usually offer bribes for concealment of offences committed',

#     # Nepotism (PDF page 5)
#     'use_facilities_family': 'The corruption digital lens can discourage organization officials from using facilities like vehicles to benefit their families',
#     'no_public_ads': 'The corruption digital lens discourages job offers that are not done through public job advertisements',
#     'same_tribe': 'The corruption digital lens discourages leaders from employing people from only one tribe in the same organization',
#     'tribe_promotions': 'The corruption digital lens mitigates against promotions of organization workers from the same tribe',
#     'unequal_pay': 'The corruption digital lens discourages against workers earning far more than their colleagues who are of the same rank',
#     'unqualified_employ': 'The corruption digital lens exposes employees without the required academic qualifications',

#     # Favoritism (PDF page 5)
#     'low_price_assets': 'The corruption digital lens mitigates against asset disposition at low prices to friends of organization workers',
#     'favor_friends': 'The corruption digital lens discourages against favouring friends and acquaintances over others in profitable activities for example contracts, promotions',
#     'no_demote_friends': 'The corruption digital lens encourages high level managers to demote or fire friends if they prove to be inefficient',
#     'political_appoint': 'The corruption digital lens mitigates appointment and promotion based on political affiliation',
#     'sex_discrimination': 'The corruption digital lens discourages sex discrimination in the recruitment and advancement process of an organization',
#     'same_religion': 'The corruption digital lens discourages most employees in an organization having the same religious affiliation',

#     # Embezzlement (PDF page 6)
#     'private_work_hours': 'The corruption digital lens mitigates people doing private work during working hours for their personal gain',
#     'theft_properties': 'The corruption digital lens discourages theft of organizational properties',
#     'theft_funds': 'The corruption digital lens mitigates theft of funds',
#     'alter_reports': 'The corruption digital lens limits accounting officers from changing figures in financial account reports for their personal gain',
#     'evade_taxes': 'The corruption digital lens discourages accounting officers from altering financial figures to avoid or evade taxes',
#     'private_use_resources': 'The corruption digital lens discourages use of agency resources for private purposes',
# }

# class Respondent(models.Model):
#     # Demographics (PDF page 1, shared)
#     GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'), ('other', 'Other(specify)')]  # PDF: tick boxes
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="1. Gender")
#     gender_other = models.CharField(max_length=100, blank=True, verbose_name="Other (specify)")

#     AGE_CHOICES = [('18-20', '18-20'), ('21-29', '21-29'), ('30-39', '30-39'), ('40-49', '40-49'), ('50+', '50 and above')]
#     age = models.CharField(max_length=10, choices=AGE_CHOICES, verbose_name="2. Age")

#     EDUCATION_CHOICES = [('certificate', 'Certificate'), ('diploma', 'Diploma'), ('bachelors', 'Bachelors'), ('masters', 'Masters'), ('phd', 'PhD')]
#     education = models.CharField(max_length=20, choices=EDUCATION_CHOICES, verbose_name="3. Highest level of Formal education")

#     RELIGION_CHOICES = [('protestant', 'Protestant'), ('catholic', 'Catholic'), ('islam', 'Islam'), ('pentecostal', 'Pentecostal'), ('other', 'Other(specify)')]
#     religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, verbose_name="5. Religious Affiliation")
#     religion_other = models.CharField(max_length=100, blank=True, verbose_name="Other (specify)")

#     EXPERIENCE_CHOICES = [('<1', '<1'), ('1-4', '1-4'), ('5-9', '5-9'), ('10+', '10+')]
#     experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES, verbose_name="6. Experience with work in the organization")

#     FAMILY_SIZE_CHOICES = [('1-3', '1-3'), ('4-6', '4-6'), ('7-9', '7-9'), ('10+', '10+')]
#     family_size = models.CharField(max_length=10, choices=FAMILY_SIZE_CHOICES, verbose_name="7. Family Size (Number of family members)")

#     MARITAL_STATUS_CHOICES = [('married', 'Married'), ('single', 'Single'), ('divorced', 'Divorced'), ('cohabiting', 'Cohabiting')]
#     marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, verbose_name="8. Marital status")

#     INCOME_CHOICES = [('1-2', '1-2'), ('3-5', '3-5'), ('6-9', '6-9'), ('10+', '10+')]
#     income = models.CharField(max_length=10, choices=INCOME_CHOICES, verbose_name="9. Income category (monthly gross salary in Millions of UGX)")

#     # Organization Demographics (PDF page 2, shared)
#     org_category = models.CharField(max_length=100, verbose_name="10. Organization Category (eg Education, security, Judiciary etc)")
#     org_age = models.CharField(max_length=10, choices=[('0-4', '0-4'), ('5-9', '5-9'), ('10-14', '10-14'), ('15-19', '15-19'), ('20+', '20+')], verbose_name="11. Organization age (in years)")
#     org_size = models.CharField(max_length=10, choices=[('<10', '<10'), ('10-49', '10-49'), ('50-99', '50-99'), ('100+', '100+')], verbose_name="12. Organization size (No of employees)")
#     org_location = models.CharField(max_length=20, choices=[('northern', 'Northern'), ('western', 'Western'), ('eastern', 'Eastern'), ('central', 'Central')], verbose_name="13. Organization Location")

#     is_post_intervention = models.BooleanField(default=False, verbose_name="Post-Intervention Survey")

#     def __str__(self):
#         return f"Respondent {self.id} - {'Post' if self.is_post_intervention else 'Initial'}"


# class EconomicResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     adequate_income = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="1: Employees in our organization have adequate-income levels")
#     economic_freedom = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="2: We have economic freedom whereby Individuals control their assets and labour without state interruptions")
#     inflation_affect = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="3: Employees’ income is affected by inflation")
#     international_trade = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="4: We freely engage in international trade activities")
#     national_trade = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="5: We freely engage in national trade activities")


# class SocialResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     social_distress = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="1: Some workers suffer from social distress")
#     social_exclusion = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="2: Social exclusion is experienced by some workers")
#     religious_beliefs = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="3: Employees have strong religious beliefs")
#     male_dominance = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="4: Majority of males take administrative/management roles compared to females")
#     middle_class_life = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="5: Most people live a life of middle-income class")
#     value_education = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="6: Our organisation values highly educated employees")
#     low_job_intensity = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="7: We have workers from families with low job intensity like families with few people having formal jobs")


# class PoliticalResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     rule_of_law = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="1: Our decisions are based on rule of Law that is individuals are subjected to the same laws")
#     state_land_control = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="2: In our country, land is controlled by the state")
#     democracy_practice = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="3: We often practise democracy in our organization")
#     political_rights = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="4: There is observance of political rights")
#     civil_liberties = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="5: We have civil liberties that is personal liberties without interference from the state")
#     fair_elections = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="6: There is freedom to choose leaders via fair elections")
#     political_stability = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="7: Political stability exists in our organisation")
#     policy_framework = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="8: We are guided by policy and institutional framework")


# class DigitalResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     digital_infra_avail = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="1: There is availability of digital infrastructure")
#     access_computers = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="2: We have access to digital infrastructure like computers")
#     support_infra = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="3: We have access to support infrastructure like internet and electricity")
#     invest_policy = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="4: We have a policy of investing in digital Technology")
#     improves_work = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="5: The use of digital technology makes work better")
#     frequent_use = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="6: We frequently use digital technologies for executing activities")


# class ParticipationResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     council_meetings = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="1: I have attended local council meetings in the past 12months")
#     discuss_policies = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="2: I take part in discussion of public policies in the country")
#     contribute_services = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="3: I contribute and deliberate on services in my country")
#     public_info = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="4: The government provides me with public information as and when demanded")
#     decision_making = models.IntegerField(choices=LIKERT_CHOICES, verbose_name="5: I engage in decision making processes of the government")


# class CorruptionResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE)
#     comments = models.TextField(blank=True, verbose_name="Other Comments")

#     # Bribery
#     public_bribes = models.IntegerField(choices=LIKERT_CHOICES)
#     request_gifts = models.IntegerField(choices=LIKERT_CHOICES)
#     convenience_bribes = models.IntegerField(choices=LIKERT_CHOICES)
#     faster_services = models.IntegerField(choices=LIKERT_CHOICES)
#     concealment_bribes = models.IntegerField(choices=LIKERT_CHOICES)

#     # Nepotism
#     use_facilities_family = models.IntegerField(choices=LIKERT_CHOICES)
#     no_public_ads = models.IntegerField(choices=LIKERT_CHOICES)
#     same_tribe = models.IntegerField(choices=LIKERT_CHOICES)
#     tribe_promotions = models.IntegerField(choices=LIKERT_CHOICES)
#     unequal_pay = models.IntegerField(choices=LIKERT_CHOICES)
#     unqualified_employ = models.IntegerField(choices=LIKERT_CHOICES)

#     # Favoritism
#     low_price_assets = models.IntegerField(choices=LIKERT_CHOICES)
#     favor_friends = models.IntegerField(choices=LIKERT_CHOICES)
#     no_demote_friends = models.IntegerField(choices=LIKERT_CHOICES)
#     political_appoint = models.IntegerField(choices=LIKERT_CHOICES)
#     sex_discrimination = models.IntegerField(choices=LIKERT_CHOICES)
#     same_religion = models.IntegerField(choices=LIKERT_CHOICES)

#     # Embezzlement
#     private_work_hours = models.IntegerField(choices=LIKERT_CHOICES)
#     theft_properties = models.IntegerField(choices=LIKERT_CHOICES)
#     theft_funds = models.IntegerField(choices=LIKERT_CHOICES)
#     alter_reports = models.IntegerField(choices=LIKERT_CHOICES)
#     evade_taxes = models.IntegerField(choices=LIKERT_CHOICES)
#     private_use_resources = models.IntegerField(choices=LIKERT_CHOICES)

#     def __init__(self, *args, **kwargs):
#         respondent = kwargs.pop('respondent', None)
#         super().__init__(*args, **kwargs)
#         if respondent:
#             self.respondent = respondent

#         if self.id:
#             labels = POST_CORRUPTION_LABELS if self.respondent and self.respondent.is_post_intervention else INITIAL_CORRUPTION_LABELS
#             for field_name, label in labels.items():
#                 field = self._meta.get_field(field_name)
#                 field.verbose_name = label



####################################################
#
# New for 3
#
###################################################




# # # models.py
# # from django.db import models

# LIKERT_CHOICES = [
#     (1, '1 - Strongly Disagree'),
#     (2, '2 - Disagree'),
#     (3, '3 - Somewhat Disagree'),
#     (4, '4 - Agree'),
#     (5, '5 - Strongly Agree'),
# ]

# # === CORRUPTION: Baseline (Pre) ===
# INITIAL_CORRUPTION_LABELS = {
#     # Bribery
#     'public_bribes': 'We have people from the public who offer bribes to organization workers',
#     'request_gifts': 'Organization workers often request for gifts or informal payments to get things done',
#     'convenience_bribes': 'In our organisation, there are people who usually offer bribes for convenience reasons',
#     'faster_services': 'People usually offer bribes to get faster services in our organisation',
#     'concealment_bribes': 'In our organisation, some people offer bribes for concealment of offences committed',

#     # Nepotism
#     'use_facilities_family': 'Organization officials use facilities like vehicles to benefit their families',
#     'no_public_ads': 'Job offers are usually not done through public job advertisements in this organisation',
#     'same_tribe': 'Most people in our organisation come from the same tribe',
#     'tribe_promotions': 'Promotions of organization workers from the same tribe takes place',
#     'unequal_pay': 'Some workers earn far more than their colleagues who are of the same rank',
#     'unqualified_employ': 'At times our organisation employs people without the required academic qualifications',

#     # Favoritism
#     'low_price_assets': 'There is asset disposition at low prices to friends of organization workers',
#     'favor_friends': 'Favouring friends and acquaintances over others in profitable activities often takes place',
#     'no_demote_friends': 'High level managers do not demote or fire friends if they prove to be inefficient',
#     'political_appoint': 'Appointment and promotion are connected to political affiliation',
#     'sex_discrimination': 'Sex discrimination at times exists in the recruitment process',
#     'same_religion': 'Most employees in our organization have the same religious affiliation',

#     # Embezzlement
#     'private_work_hours': 'Some people do private work during working hours for their personal gain',
#     'theft_properties': 'There is theft of organizational properties',
#     'theft_funds': 'There is theft of funds in our organization',
#     'alter_reports': 'Some accounting officers change figures in financial account reports for their personal gain',
#     'evade_taxes': 'Some accounting officers sometimes alter financial figures to avoid or evade taxes',
#     'private_use_resources': 'Agency resources are Often used for private purposes',
# }

# # === CORRUPTION: Post-intervention (After Digital Lens) ===
# POST_CORRUPTION_LABELS = {
#     # Bribery
#     'public_bribes': 'The corruption digital lens (system) can mitigate bribes offered by the public to organization workers',
#     'request_gifts': 'The corruption digital lens minimises the request for gifts or informal payments by organization workers from the public to get things done',
#     'convenience_bribes': 'The corruption digital lens can discourage people who usually offer bribes for convenience reasons',
#     'faster_services': 'The corruption digital lens can minimise the rate at which people usually offer bribes to get faster services',
#     'concealment_bribes': 'The corruption digital lens can discourage people who usually offer bribes for concealment of offences committed',

#     # Nepotism
#     'use_facilities_family': 'The corruption digital lens can discourage organization officials from using facilities like vehicles to benefit their families',
#     'no_public_ads': 'The corruption digital lens discourages job offers that are not done through public job advertisements',
#     'same_tribe': 'The corruption digital lens discourages leaders from employing people from only one tribe in the same organization',
#     'tribe_promotions': 'The corruption digital lens mitigates against promotions of organization workers from the same tribe',
#     'unequal_pay': 'The corruption digital lens discourages against workers earning far more than their colleagues who are of the same rank',
#     'unqualified_employ': 'The corruption digital lens exposes employees without the required academic qualifications',

#     # Favoritism
#     'low_price_assets': 'The corruption digital lens mitigates against asset disposition at low prices to friends of organization workers',
#     'favor_friends': 'The corruption digital lens discourages against favouring friends and acquaintances over others in profitable activities for example contracts, promotions',
#     'no_demote_friends': 'The corruption digital lens encourages high level managers to demote or fire friends if they prove to be inefficient',
#     'political_appoint': 'The corruption digital lens mitigates appointment and promotion based on political affiliation',
#     'sex_discrimination': 'The corruption digital lens discourages sex discrimination in the recruitment and advancement process of an organization',
#     'same_religion': 'The corruption digital lens discourages most employees in an organization having the same religious affiliation',

#     # Embezzlement
#     'private_work_hours': 'The corruption digital lens mitigates people doing private work during working hours for their personal gain',
#     'theft_properties': 'The corruption digital lens discourages theft of organizational properties',
#     'theft_funds': 'The corruption digital lens mitigates theft of funds',
#     'alter_reports': 'The corruption digital lens limits accounting officers from changing figures in financial account reports for their personal gain',
#     'evade_taxes': 'The corruption digital lens discourages accounting officers from altering financial figures to avoid or evade taxes',
#     'private_use_resources': 'The corruption digital lens discourages use of agency resources for private purposes',
# }

# # === NEW: Knowledge/Perception of Digital Lens (Questionnaire 3) ===
# KNOWLEDGE_CORRUPTION_LABELS = POST_CORRUPTION_LABELS  # Same wording as Post-intervention


# class Respondent(models.Model):
#     SURVEY_TYPE_CHOICES = [
#         ('baseline', 'Baseline (Pre-Intervention)'),
#         ('post', 'Post-Intervention (After Digital Lens)'),
#         ('knowledge', 'Knowledge/Perception of Digital Lens'),
#     ]

#     survey_type = models.CharField(max_length=20, choices=SURVEY_TYPE_CHOICES, default='baseline')

#     # Demographics – 100% match with final questionnaire
#     GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'), ('other', 'Other(specify)')]
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="1. Gender")
#     gender_other = models.CharField(max_length=100, blank=True, verbose_name="Other(specify)")

#     AGE_CHOICES = [('18-20', '18-20'), ('21-29', '21-29'), ('30-39', '30-39'), ('40-49', '40-49'), ('50+', '50 and above')]
#     age = models.CharField(max_length=10, choices=AGE_CHOICES, verbose_name="2. Age")

#     EDUCATION_CHOICES = [('certificate', 'Certificate'), ('diploma', 'Diploma'), ('bachelors', 'Bachelors'),
#                          ('pgd', 'PGD'), ('masters', 'Masters'), ('phd', 'PhD')]
#     education = models.CharField(max_length=20, choices=EDUCATION_CHOICES, verbose_name="3. Highest level of Formal education")

#     RELIGION_CHOICES = [('protestant', 'Protestant'), ('catholic', 'Catholic'), ('islam', 'Islam'),
#                         ('pentecostal', 'Pentecostal'), ('other', 'Other(specify)')]
#     religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, verbose_name="5. Religious Affiliation")
#     religion_other = models.CharField(max_length=100, blank=True, verbose_name="Other(specify)")

#     experience = models.CharField(max_length=10, choices=[('<1', '<1'), ('1-4', '1-4'), ('5-9', '5-9'), ('10+', '10+ years')],
#                                   verbose_name="6. Experience with work in the organization (years)")
#     family_size = models.CharField(max_length=10, choices=[('1-3', '1-3'), ('4-6', '4-6'), ('7-9', '7-9'), ('10+', '10+')],
#                                    verbose_name="7. Family Size (Number of family members)")
#     marital_status = models.CharField(max_length=20, choices=[('married', 'Married'), ('single', 'Single'),
#                                                               ('divorced', 'Divorced'), ('cohabiting', 'Cohabiting')],
#                                       verbose_name="8. Marital status")
#     income = models.CharField(max_length=10, choices=[('1-2', '1-2'), ('3-5', '3-5'), ('6-9', '6-9'), ('10+', '10+')],
#                               verbose_name="9. Income category (monthly gross salary in Millions of UGX)")

#     org_category = models.CharField(max_length=100, verbose_name="10. Organization Category")
#     org_age = models.CharField(max_length=10, choices=[('0-4', '0-4'), ('5-9', '5-9'), ('10-14', '10-14'),
#                                                        ('15-19', '15-19'), ('20+', '20+')], verbose_name="11. Organization age (in years)")
#     org_size = models.CharField(max_length=10, choices=[('<10', '<10'), ('10-49', '10-49'), ('50-99', '50-99'), ('100+', '100+')],
#                                 verbose_name="12. Organization size (No of employees)")
#     org_location = models.CharField(max_length=20, choices=[('northern', 'Northern'), ('western', 'Western'),
#                                                             ('eastern', 'Eastern'), ('central', 'Central')],
#                                     verbose_name="13. Organization Location")

#     def __str__(self):
#         return f"{self.get_survey_type_display()} - Respondent {self.id}"


# # Section B – Only for Baseline
# class EconomicResponse(models.Model): respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE, related_name='economic')
# class SocialResponse(models.Model): respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE, related_name='social')
# class PoliticalResponse(models.Model): respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE, related_name='political')
# class DigitalResponse(models.Model): respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE, related_name='digital')
# class ParticipationResponse(models.Model): respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE, related_name='participation')

# # Corruption – Used by ALL THREE questionnaires
# class CorruptionResponse(models.Model):
#     respondent = models.OneToOneField(Respondent, on_delete=models.CASCADE, related_name='corruption')
#     comments = models.TextField(blank=True, verbose_name="Other Comments")

#     # All 22 corruption items (same fields, different labels)
#     public_bribes = models.IntegerField(choices=LIKERT_CHOICES)
#     request_gifts = models.IntegerField(choices=LIKERT_CHOICES)
#     convenience_bribes = models.IntegerField(choices=LIKERT_CHOICES)
#     faster_services = models.IntegerField(choices=LIKERT_CHOICES)
#     concealment_bribes = models.IntegerField(choices=LIKERT_CHOICES)

#     use_facilities_family = models.IntegerField(choices=LIKERT_CHOICES)
#     no_public_ads = models.IntegerField(choices=LIKERT_CHOICES)
#     same_tribe = models.IntegerField(choices=LIKERT_CHOICES)
#     tribe_promotions = models.IntegerField(choices=LIKERT_CHOICES)
#     unequal_pay = models.IntegerField(choices=LIKERT_CHOICES)
#     unqualified_employ = models.IntegerField(choices=LIKERT_CHOICES)

#     low_price_assets = models.IntegerField(choices=LIKERT_CHOICES)
#     favor_friends = models.IntegerField(choices=LIKERT_CHOICES)
#     no_demote_friends = models.IntegerField(choices=LIKERT_CHOICES)
#     political_appoint = models.IntegerField(choices=LIKERT_CHOICES)
#     sex_discrimination = models.IntegerField(choices=LIKERT_CHOICES)
#     same_religion = models.IntegerField(choices=LIKERT_CHOICES)

#     private_work_hours = models.IntegerField(choices=LIKERT_CHOICES)
#     theft_properties = models.IntegerField(choices=LIKERT_CHOICES)
#     theft_funds = models.IntegerField(choices=LIKERT_CHOICES)
#     alter_reports = models.IntegerField(choices=LIKERT_CHOICES)
#     evade_taxes = models.IntegerField(choices=LIKERT_CHOICES)
#     private_use_resources = models.IntegerField(choices=LIKERT_CHOICES)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         # Dynamically set verbose_name after save
#         labels = {
#             'baseline': INITIAL_CORRUPTION_LABELS,
#             'post': POST_CORRUPTION_LABELS,
#             'knowledge': KNOWLEDGE_CORRUPTION_LABELS,
#         }[self.respondent.survey_type]
#         for field_name, label in labels.items():
#             self._meta.get_field(field_name).verbose_name = label















# models.py
# from django.db import models
# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

LIKERT_CHOICES = [
    (1, 'Strongly Disagree'),
    (2, 'Disagree'),
    (3, 'Somewhat Agree'),
    (4, 'Agree'),
    (5, 'Strongly Agree'),
]

GENDER_CHOICES = [
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Others (specify)'),
]

AGE_CHOICES = [
    (1, '18-20'),
    (2, '21-29'),
    (3, '30-39'),
    (4, '40-49'),
    (5, '50 and above'),
]

EDUCATION_CHOICES = [
    (1, 'Certificate'),
    (2, 'Diploma'),
    (3, 'Bachelors'),
    (4, 'PGD/Masters'),
    (5, 'PhD'),
]

RELIGION_CHOICES = [
    (1, 'Protestant'),
    (2, 'Catholic'),
    (3, 'Islam'),
    (4, 'Pentecostal'),
    (5, 'Others (specify)'),
]

EXPERIENCE_CHOICES = [
    (1, '<1'),
    (2, '1-4'),
    (3, '5-9'),
    (4, '10+ years'),
]

FAMILY_SIZE_CHOICES = [
    (1, '1-3'),
    (2, '4-6'),
    (3, '7-9'),
    (4, '10+'),
]

MARITAL_CHOICES = [
    (1, 'Married'),
    (2, 'Single'),
    (3, 'Divorced'),
    (4, 'Re-married'),
    (5, 'Cohabiting'),
]

PUBLIC_INCOME_CHOICES = [
    (1, '<1'),
    (2, '1-2'),
    (3, '3-5'),
    (4, '6-9'),
    (5, '10+'),
]

EMPLOYEE_INCOME_CHOICES = [
    (1, '1-2'),
    (2, '3-5'),
    (3, '6-9'),
    (4, '10+'),
]

ORG_AGE_CHOICES = [
    (1, '0-4'),
    (2, '5-9'),
    (3, '10-14'),
    (4, '15-19'),
    (5, '20+'),
]

ORG_SIZE_CHOICES = [
    (1, '<10'),
    (2, '10-49'),
    (3, '50-99'),
    (4, '100+'),
]

ORG_LOCATION_CHOICES = [
    (1, 'Northern'),
    (2, 'Western'),
    (3, 'Eastern'),
    (4, 'Central'),
]

class BaseResponse(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, verbose_name="Other Comments")

    class Meta:
        abstract = True

class SystemResponse(BaseResponse):
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name="1. Gender")
    gender_other = models.CharField(max_length=100, blank=True, verbose_name="Gender (others specify)")
    age = models.IntegerField(choices=AGE_CHOICES, verbose_name="2. Age")
    education = models.IntegerField(choices=EDUCATION_CHOICES, verbose_name="3. Highest level of Formal education")
    religion = models.IntegerField(choices=RELIGION_CHOICES, verbose_name="5. Religious Affiliation")
    religion_other = models.CharField(max_length=100, blank=True, verbose_name="Religious Affiliation (others specify)")
    experience = models.IntegerField(choices=EXPERIENCE_CHOICES, verbose_name="6. Experience with work in the organization")
    family_size = models.IntegerField(choices=FAMILY_SIZE_CHOICES, verbose_name="7. Family Size (Number of family members)")
    marital = models.IntegerField(choices=MARITAL_CHOICES, verbose_name="8. Marital status")
    income = models.IntegerField(choices=EMPLOYEE_INCOME_CHOICES, verbose_name="9. Income category (monthly gross salary in Millions of UGX)")
    org_category = models.CharField(max_length=200, verbose_name="10. Organization Category (eg Education, security, Judiciary etc)")
    org_age = models.IntegerField(choices=ORG_AGE_CHOICES, verbose_name="11. Organization age (in years)")
    org_size = models.IntegerField(choices=ORG_SIZE_CHOICES, verbose_name="12. Organization size (No of employees)")
    org_location = models.IntegerField(choices=ORG_LOCATION_CHOICES, verbose_name="13. Organization Location")
    bribery_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: The corruption digital lens (system) can mitigate bribes offered by the public to organization workers")
    bribery_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: The corruption digital lens minimises the request for gifts or informal payments by organization workers from the public to get things done")
    bribery_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: The corruption digital lens can discourage people who usually offer bribes for convenience reasons")
    bribery_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: The corruption digital lens can minimise the rate at which people usually offer bribes to get faster services")
    bribery_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: The corruption digital lens can discourage people who usually offer bribes for concealment of offences committed")
    nepotism_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: The corruption digital lens can discourage organization officials from using facilities like vehicles to benefit their families")
    nepotism_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: The corruption digital lens discourages job offers that are not done through public job advertisements")
    nepotism_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: The corruption digital lens discourages leaders from employing people from only one tribe in the same organization")
    nepotism_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: The corruption digital lens mitigates against promotions of organization workers to different levels from the same tribe")
    nepotism_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: The corruption digital lens discourages against workers earning far more than their colleagues who are of the same rank")
    nepotism_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: The corruption digital lens discourages employers from recruiting employees without the required academic qualifications")
    favoritism_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: The corruption digital lens mitigates against asset disposition at low prices to friends of organization workers")
    favoritism_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: The corruption digital lens discourages against favouring friends and acquaintances over others in profitable activities for example contracts, promotions")
    favoritism_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: The corruption digital lens encourages high level managers to demote or fire friends if they prove to be inefficient")
    favoritism_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: The corruption digital lens mitigates appointment and promotion based on political affiliation")
    favoritism_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: The corruption digital lens discourages sex discrimination in the recruitment and advancement process of an organization")
    favoritism_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: The corruption digital lens discourages most employees in an organization having the same religious affiliation")
    embezzlement_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: The corruption digital lens mitigates people doing private work during working hours for their personal gain")
    embezzlement_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: The corruption digital lens discourages theft of organizational properties")
    embezzlement_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: The corruption digital lens mitigates theft of funds")
    embezzlement_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: The corruption digital lens limits accounting officers from changing figures in financial account reports for their personal gain")
    embezzlement_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: The corruption digital lens discourages accounting officers from altering financial figures to avoid or evade taxes")
    embezzlement_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: The corruption digital lens discourages use of agency resources for private purposes")

class PublicResponse(BaseResponse):
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name="1. Gender")
    gender_other = models.CharField(max_length=100, blank=True, verbose_name="Gender (others specify)")
    age = models.IntegerField(choices=AGE_CHOICES, verbose_name="2. Age")
    education = models.IntegerField(choices=EDUCATION_CHOICES, verbose_name="3. Highest level of Formal education")
    religion = models.IntegerField(choices=RELIGION_CHOICES, verbose_name="5. Religious Affiliation")
    religion_other = models.CharField(max_length=100, blank=True, verbose_name="Religious Affiliation (others specify)")
    experience = models.IntegerField(choices=EXPERIENCE_CHOICES, verbose_name="6. Experience with work in the public organization")
    family_size = models.IntegerField(choices=FAMILY_SIZE_CHOICES, verbose_name="7. Family Size (Number of family members)")
    marital = models.IntegerField(choices=MARITAL_CHOICES, verbose_name="8. Marital status")
    income = models.IntegerField(choices=PUBLIC_INCOME_CHOICES, verbose_name="9. Income category (monthly gross income in Millions of UGX)")
    org_name = models.CharField(max_length=250, verbose_name="10. Organization Name", null=True, blank=True)
    org_category = models.CharField(max_length=200, verbose_name="11. Organization Category (eg Education, security, Judiciary, local government etc)")
    org_age = models.IntegerField(choices=ORG_AGE_CHOICES, verbose_name="12. Organization age (in years)")
    org_size = models.IntegerField(choices=ORG_SIZE_CHOICES, verbose_name="13. Organization size (No of employees)")
    org_location = models.IntegerField(choices=ORG_LOCATION_CHOICES, verbose_name="14. Organization Location")
    economic_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Employees in public organizations/sector have adequate-income levels")
    economic_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: Employees have economic freedom whereby Individuals control their assets and labour without state interruptions")
    economic_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: Employees’ income is affected by inflation")
    economic_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Employees engage in international trade activities")
    economic_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Employees engage in national trade activities")
    social_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Some workers suffer from social distress")
    social_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2. Social exclusion is experienced by some workers")
    social_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: Employees have strong religious beliefs")
    social_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Majority of males take administrative/management roles compared to females")
    social_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Most people in public organizations live a life of middle-income class")
    social_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: Public organisations value highly educated employees")
    social_7 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="7: Some public organisations have workers from families with low job intensity like families with few people having formal jobs")
    political_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Decisions in public organizations are based on rule of Law")
    political_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: In our country, land is controlled by the state")
    political_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: Public organisations often practise democracy")
    political_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: There is observance of political rights")
    political_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Public organisations have civil liberties without interference from the state")
    political_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: There is freedom to choose leaders via fair election")
    political_7 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="7: Political stability exists in public organisations")
    political_8 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="8: Public organisations are guided by policy and institutional framework")
    digital_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: There is availability of digital infrastructure in public organisations")
    digital_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: Employees have access to digital infrastructure like computers")
    digital_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: Employees have access to support infrastructure like internet and electricity")
    digital_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Employees have a policy of investing in digital Technology")
    digital_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: The use of digital technology makes work better for employees")
    digital_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: Employees frequently use digital technologies for executing activities")
    civic_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: I have attended local council meetings in the past 12months")
    civic_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: I take part in discussion of public policies in the country")
    civic_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: I contribute and deliberate on services in my country")
    civic_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: The government provides me with public information as and when demanded")
    civic_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: I engage in decision making processes of the government")
    corruption_bribery_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: We have people from the public who offer bribes to organization workers")
    corruption_bribery_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: Organization workers often request for gifts or informal payments to get things done")
    corruption_bribery_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: In public organisations, there are people who usually offer bribes for convenience reasons")
    corruption_bribery_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: People usually offer bribes to get faster services in public organisations")
    corruption_bribery_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: In public organisations, some people offer bribes for concealment of offences committed")
    corruption_nepotism_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Organization officials use facilities like vehicles to benefit their families")
    corruption_nepotism_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: Job offers are usually not done through public job advertisements in public organisations")
    corruption_nepotism_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: Most people in public organisations come from the same tribe/region")
    corruption_nepotism_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Promotions of organization workers to different levels from the same tribe takes place in public organisations")
    corruption_nepotism_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Some workers earn far more than their colleagues who are of the same rank")
    corruption_nepotism_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: At times public organisations employ people without the required academic qualifications")
    corruption_favoritism_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: There is asset disposition at low prices to friends of organization workers")
    corruption_favoritism_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: Favouring friends and acquaintances over others in profitable activities often takes place")
    corruption_favoritism_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: High level managers do not demote or fire friends if they prove to be inefficient")
    corruption_favoritism_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Appointment and promotion are connected to political affiliation")
    corruption_favoritism_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Sex discrimination at times exists in the recruitment process")
    corruption_favoritism_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: Most employees in public organizations have the same religious affiliation")
    corruption_embezzlement_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Some people in public organizations do private work during working hours for their personal gain")
    corruption_embezzlement_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: There is theft of organizational properties by employees")
    corruption_embezzlement_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: There is theft of funds in public organizations")
    corruption_embezzlement_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Some accounting officers change figures in financial account reports for their personal gain")
    corruption_embezzlement_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Some accounting officers sometimes alter financial figures to avoid or evade taxes")
    corruption_embezzlement_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: Public organisation resources are often used for private purposes")

class EmployeeResponse(BaseResponse):
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name="1. Gender")
    gender_other = models.CharField(max_length=100, blank=True, verbose_name="Gender (others specify)")
    age = models.IntegerField(choices=AGE_CHOICES, verbose_name="2. Age")
    education = models.IntegerField(choices=EDUCATION_CHOICES, verbose_name="3. Highest level of Formal education")
    religion = models.IntegerField(choices=RELIGION_CHOICES, verbose_name="5. Religious Affiliation")
    religion_other = models.CharField(max_length=100, blank=True, verbose_name="Religious Affiliation (others specify)")
    experience = models.IntegerField(choices=EXPERIENCE_CHOICES, verbose_name="6. Experience with work in the organization")
    family_size = models.IntegerField(choices=FAMILY_SIZE_CHOICES, verbose_name="7. Family Size (Number of family members)")
    marital = models.IntegerField(choices=MARITAL_CHOICES, verbose_name="8. Marital status")
    income = models.IntegerField(choices=EMPLOYEE_INCOME_CHOICES, verbose_name="9. Income category (monthly gross salary in Millions of UGX)")
    org_name = models.CharField(max_length=250, verbose_name="10. Organization Name", null=True, blank=True)
    org_category = models.CharField(max_length=200, verbose_name="11. Organization Category (eg Education, security, Judiciary etc)")
    org_age = models.IntegerField(choices=ORG_AGE_CHOICES, verbose_name="12. Organization age (in years)")
    org_size = models.IntegerField(choices=ORG_SIZE_CHOICES, verbose_name="13. Organization size (No of employees)")
    org_location = models.IntegerField(choices=ORG_LOCATION_CHOICES, verbose_name="14. Organization Location")
    economic_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Employees in our organization have adequate-income levels")
    economic_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: We have economic freedom whereby Individuals control their assets and labour without state interruptions")
    economic_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: Employees’ income is affected by inflation")
    economic_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: We freely engage in international trade activities")
    economic_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: We freely engage in national trade activities")
    social_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Some workers suffer from social distress")
    social_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2. Social exclusion is experienced by some workers")
    social_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: Employees have strong religious beliefs")
    social_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Majority of males take administrative/management roles compared to females")
    social_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Most people live a life of middle-income class")
    social_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: Our organisation values highly educated employees")
    social_7 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="7: We have workers from families with low job intensity like families with few people having formal jobs")
    political_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Our decisions are based on rule of Law- individuals are subjected to the same laws")
    political_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: In our country, land is controlled by the state")
    political_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: We often practise democracy in our organization")
    political_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: There is observance of political rights")
    political_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: We have civil liberties- personal liberties without interference from the state")
    political_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: There is freedom to choose leaders via fair elections")
    political_7 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="7: Political stability exists in our organisation")
    political_8 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="8: We are guided by policy and institutional framework")
    digital_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: There is availability of digital infrastructure")
    digital_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: We have access to digital infrastructure like computers")
    digital_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: We have access to support infrastructure like internet and electricity")
    digital_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: We have a policy of investing in digital Technology")
    digital_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: The use of digital technology makes work better")
    digital_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: We frequently use digital technologies for executing activities")
    civic_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: I have attended local council meetings in the past 12months")
    civic_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: I take part in discussion of public policies in the country")
    civic_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: I contribute and deliberate on services in my country")
    civic_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: The government provides me with public information as and when demanded")
    civic_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: I engage in decision making processes of the government")
    corruption_bribery_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: We have people from the public who offer bribes to organization workers")
    corruption_bribery_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: Organization workers often request for gifts or informal payments to get things done")
    corruption_bribery_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: In our organisation, there are people who usually offer bribes for convenience reasons")
    corruption_bribery_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: People usually offer bribes to get faster services in our organisation")
    corruption_bribery_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: In our organisation, some people offer bribes for concealment of offences committed")
    corruption_nepotism_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Organization officials use facilities like vehicles to benefit their families")
    corruption_nepotism_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: Job offers are usually not done through public job advertisements in this organisation")
    corruption_nepotism_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: Most people in our organisation come from the same tribe")
    corruption_nepotism_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Promotions of organization workers to different levels from the same tribe takes place")
    corruption_nepotism_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Some workers earn far more than their colleagues who are of the same rank")
    corruption_nepotism_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: At times our organisation employs people without the required academic qualifications")
    corruption_favoritism_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: There is asset disposition at low prices to friends of organization workers")
    corruption_favoritism_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: Favouring friends and acquaintances over others in profitable activities often takes place")
    corruption_favoritism_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: High level managers do not demote or fire friends if they prove to be inefficient")
    corruption_favoritism_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Appointment and promotion are connected to political affiliation")
    corruption_favoritism_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Sex discrimination at times exists in the recruitment process")
    corruption_favoritism_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: Most employees in our organization have the same religious affiliation")
    corruption_embezzlement_1 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="1: Some people do private work during working hours for their personal gain")
    corruption_embezzlement_2 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="2: There is theft of organizational properties")
    corruption_embezzlement_3 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="3: There is theft of funds in our organization")
    corruption_embezzlement_4 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="4: Some accounting officers change figures in financial account reports for their personal gain")
    corruption_embezzlement_5 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="5: Some accounting officers sometimes alter financial figures to avoid or evade taxes")
    corruption_embezzlement_6 = models.IntegerField(choices=LIKERT_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="6: Organisation resources are often used for private purposes")
