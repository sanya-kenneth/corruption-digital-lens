from django.contrib import admin
from .models import CorruptionForm, Factor, Act, Comment, Incident


class CorruptionFormAdmin(admin.ModelAdmin):
    list_display = ('name', '_description')
    search_fields = ("name",)

    def _description(self, obj):
        return f"{obj.description[:150]}..." if len(obj.description) >= 150 else obj.description
    _description.short_description = 'Description'


class FactorAdmin(admin.ModelAdmin):
    list_display = ("name", "_description")
    search_fields = ("name",)
    
    def _description(self, obj):
        return f"{obj.description[:150]}..." if len(obj.description) >= 150 else obj.description
    _description.short_description = 'Description'


class ActAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "notes","interplay", "likes")
    search_fields = ("name",)
    readonly_fields = ("likes",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "created_at")
    readonly_fields = ("comment", "created_at")
    
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("form_of_corruption", "location", "description", "email")
    readonly_fields = ("form_of_corruption", "location", "description", "email")
    

admin.site.register(CorruptionForm, CorruptionFormAdmin)
admin.site.register(Factor, FactorAdmin)
admin.site.register(Act, ActAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Incident, IncidentAdmin)
    