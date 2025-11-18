from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import CorruptionForm, CorruptionPage, Factor, Act, Comment, Incident, Feedback, Interplay, InterplayComment
from django.db import models
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import SystemResponse, PublicResponse, EmployeeResponse


class CorruptionFormAdmin(admin.ModelAdmin):
    list_display = ('name', '_description')
    search_fields = ("name",)

    def _description(self, obj):
        return f"{obj.description[:150]}..." if len(obj.description) >= 150 else obj.description
    _description.short_description = 'Description'
    
    class AdminConfig:
        ordering = "Core Content"


class FactorAdmin(admin.ModelAdmin):
    list_display = ("name", "_description")
    search_fields = ("name",)
    formfield_overrides = {
        models.TextField: {'required': False},
    }

    def _description(self, obj):
        return f"{obj.description[:150]}..." if len(obj.description) >= 150 else obj.description
    _description.short_description = 'Description'
    
    class AdminConfig:
        ordering = "Core Content"


class ActAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "notes",
                    "interplay", "references", "likes")
    search_fields = ("name",)
    readonly_fields = ("likes",)
    formfield_overrides = {
        models.TextField: {'required': False},
    }
    
    class AdminConfig:
        ordering = "Core Content"


class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "act", "created_at")
    readonly_fields = ("comment", "act", "created_at")
    
    class AdminConfig:
        ordering = "User Submissions"


class IncidentAdmin(admin.ModelAdmin):
    list_display = ("form_of_corruption", "location", "description", "email")
    readonly_fields = ("form_of_corruption", "location",
                       "description", "email")
    
    class AdminConfig:
        ordering = "User Submissions"


class InterplayAdmin(admin.ModelAdmin):
    # list_display = '__all__'
    readonly_fields = ('likes',)
    
    class AdminConfig:
        ordering = "Core Content"


class InterplayCommentAdmin(admin.ModelAdmin):
    list_display = ('interplay', 'comment')
    readonly_fields = ('interplay', 'comment')
    
    class AdminConfig:
        ordering = "User Submissions"


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback_type', 'message')
    
    class AdminConfig:
        ordering = "User Submissions"


@admin.register(SystemResponse)
class SystemResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    fieldsets = [
        ('Demographics', {'fields': ['gender', 'gender_other', 'age', 'education', 'religion', 'religion_other',
         'experience', 'family_size', 'marital', 'income', 'org_category', 'org_age', 'org_size', 'org_location']}),
        ('Bribery Mitigation', {'fields': [
         'bribery_1', 'bribery_2', 'bribery_3', 'bribery_4', 'bribery_5']}),
        ('Nepotism Mitigation', {'fields': [
         'nepotism_1', 'nepotism_2', 'nepotism_3', 'nepotism_4', 'nepotism_5', 'nepotism_6']}),
        ('Favoritism Mitigation', {'fields': [
         'favoritism_1', 'favoritism_2', 'favoritism_3', 'favoritism_4', 'favoritism_5', 'favoritism_6']}),
        ('Embezzlement Mitigation', {'fields': [
         'embezzlement_1', 'embezzlement_2', 'embezzlement_3', 'embezzlement_4', 'embezzlement_5', 'embezzlement_6']}),
        ('Comment', {'fields': ['comment']}),
    ]

    class AdminConfig:
        ordering = "Questionnaires"


@admin.register(PublicResponse)
class PublicResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    fieldsets = [
        ('Demographics', {'fields': ['gender', 'gender_other', 'age', 'education', 'religion', 'religion_other',
         'experience', 'family_size', 'marital', 'income', 'org_category', 'org_age', 'org_size', 'org_location']}),
        ('Part 1: Economic Factors', {'fields': [
         'economic_1', 'economic_2', 'economic_3', 'economic_4', 'economic_5']}),
        ('Part 2: Social Factors', {'fields': [
         'social_1', 'social_2', 'social_3', 'social_4', 'social_5', 'social_6', 'social_7']}),
        ('Part 3: Political Factors', {'fields': [
         'political_1', 'political_2', 'political_3', 'political_4', 'political_5', 'political_6', 'political_7', 'political_8']}),
        ('Part 4: Digital Factors', {'fields': [
         'digital_1', 'digital_2', 'digital_3', 'digital_4', 'digital_5', 'digital_6']}),
        ('Part 5: Civic Engagement', {'fields': [
         'civic_1', 'civic_2', 'civic_3', 'civic_4', 'civic_5']}),
        ('Part 6: Level of Corruption - Bribery',
         {'fields': ['corruption_bribery_1', 'corruption_bribery_2', 'corruption_bribery_3', 'corruption_bribery_4', 'corruption_bribery_5']}),
        ('Part 6: Level of Corruption - Nepotism', {'fields': ['corruption_nepotism_1', 'corruption_nepotism_2',
         'corruption_nepotism_3', 'corruption_nepotism_4', 'corruption_nepotism_5', 'corruption_nepotism_6']}),
        ('Part 6: Level of Corruption - Favoritism', {'fields': ['corruption_favoritism_1', 'corruption_favoritism_2',
         'corruption_favoritism_3', 'corruption_favoritism_4', 'corruption_favoritism_5', 'corruption_favoritism_6']}),
        ('Part 6: Level of Corruption - Embezzlement', {'fields': ['corruption_embezzlement_1', 'corruption_embezzlement_2',
         'corruption_embezzlement_3', 'corruption_embezzlement_4', 'corruption_embezzlement_5', 'corruption_embezzlement_6']}),
        ('Comment', {'fields': ['comment']}),
    ]

    class AdminConfig:
        ordering = "Questionnaires"


@admin.register(EmployeeResponse)
class EmployeeResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    fieldsets = [
        ('Demographics', {'fields': ['gender', 'gender_other', 'age', 'education', 'religion', 'religion_other',
         'experience', 'family_size', 'marital', 'income', 'org_category', 'org_age', 'org_size', 'org_location']}),
        ('Part 1: Economic Factors', {'fields': [
         'economic_1', 'economic_2', 'economic_3', 'economic_4', 'economic_5']}),
        ('Part 2: Social Factors', {'fields': [
         'social_1', 'social_2', 'social_3', 'social_4', 'social_5', 'social_6', 'social_7']}),
        ('Part 3: Political Factors', {'fields': [
         'political_1', 'political_2', 'political_3', 'political_4', 'political_5', 'political_6', 'political_7', 'political_8']}),
        ('Part 4: Digital Factors', {'fields': [
         'digital_1', 'digital_2', 'digital_3', 'digital_4', 'digital_5', 'digital_6']}),
        ('Part 5: Civic Engagement', {'fields': [
         'civic_1', 'civic_2', 'civic_3', 'civic_4', 'civic_5']}),
        ('Part 6: Level of Corruption - Bribery',
         {'fields': ['corruption_bribery_1', 'corruption_bribery_2', 'corruption_bribery_3', 'corruption_bribery_4', 'corruption_bribery_5']}),
        ('Part 6: Level of Corruption - Nepotism', {'fields': ['corruption_nepotism_1', 'corruption_nepotism_2',
         'corruption_nepotism_3', 'corruption_nepotism_4', 'corruption_nepotism_5', 'corruption_nepotism_6']}),
        ('Part 6: Level of Corruption - Favoritism', {'fields': ['corruption_favoritism_1', 'corruption_favoritism_2',
         'corruption_favoritism_3', 'corruption_favoritism_4', 'corruption_favoritism_5', 'corruption_favoritism_6']}),
        ('Part 6: Level of Corruption - Embezzlement', {'fields': ['corruption_embezzlement_1', 'corruption_embezzlement_2',
         'corruption_embezzlement_3', 'corruption_embezzlement_4', 'corruption_embezzlement_5', 'corruption_embezzlement_6']}),
        ('Comment', {'fields': ['comment']}),
    ]

    class AdminConfig:
        ordering = "Questionnaires"


# class ExportAllAdmin(BaseResponseAdmin):
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('export-all/', self.admin_site.admin_view(self.export_all_view), name='export-all'),
#         ]
#         return custom_urls + urls

#     def export_all_view(self, request):
#         queryset = self.model.objects.all()
#         return export_to_excel(self, request, queryset)

# # Then replace the admin registration:
# admin.site.unregister(SystemResponse)
# admin.site.unregister(PublicResponse)
# admin.site.unregister(EmployeeResponse)

# @admin.register(SystemResponse)
# class SystemResponseAdmin(ExportAllAdmin):
#     pass

# @admin.register(PublicResponse)
# class PublicResponseAdmin(ExportAllAdmin):
#     pass

# @admin.register(EmployeeResponse)
# class EmployeeResponseAdmin(ExportAllAdmin):
#     pass


def comments_preview(self, obj):
    if not obj.comments:
        return "-"
    return obj.comments[:50] + ("..." if len(obj.comments) > 50 else "")


comments_preview.short_description = "Comments"

# Custom AdminSite for reordering + sections

admin.site.register(CorruptionForm, CorruptionFormAdmin)
admin.site.register(Factor, FactorAdmin)
admin.site.register(Act, ActAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Interplay, InterplayAdmin)
admin.site.register(InterplayComment, InterplayCommentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(CorruptionPage)
