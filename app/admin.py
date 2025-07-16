from django.contrib import admin
from .models import CorruptionForm, CorruptionPage, Factor, Act, Comment, Incident, Feedback, Interplay, InterplayComment
from django.db import models


class CorruptionFormAdmin(admin.ModelAdmin):
    list_display = ('name', '_description')
    search_fields = ("name",)

    def _description(self, obj):
        return f"{obj.description[:150]}..." if len(obj.description) >= 150 else obj.description
    _description.short_description = 'Description'


class FactorAdmin(admin.ModelAdmin):
    list_display = ("name", "_description")
    search_fields = ("name",)
    formfield_overrides = {
        models.TextField: {'required': False},
    }
    
    def _description(self, obj):
        return f"{obj.description[:150]}..." if len(obj.description) >= 150 else obj.description
    _description.short_description = 'Description'


class ActAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "notes","interplay", "references", "likes")
    search_fields = ("name",)
    readonly_fields = ("likes",)
    formfield_overrides = {
        models.TextField: {'required': False},
    }

class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "act", "created_at")
    readonly_fields = ("comment", "act", "created_at")
    
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("form_of_corruption", "location", "description", "email")
    readonly_fields = ("form_of_corruption", "location", "description", "email")
    

class InterplayAdmin(admin.ModelAdmin):
    # list_display = '__all__'
    readonly_fields = ('likes',)
    
class InterplayCommentAdmin(admin.ModelAdmin):
    list_display = ('interplay', 'comment')
    readonly_fields = ('interplay', 'comment')
    
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback_type', 'message')
    

admin.site.register(CorruptionForm, CorruptionFormAdmin)
admin.site.register(Factor, FactorAdmin)
admin.site.register(Act, ActAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Interplay, InterplayAdmin)
admin.site.register(InterplayComment, InterplayCommentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(CorruptionPage)
  