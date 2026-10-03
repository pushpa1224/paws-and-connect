from django.contrib import admin
from .models import AdoptionRequest


@admin.action(description='Approve selected adoption requests')
def approve_requests(modeladmin, request, queryset):
    for obj in queryset:
        if obj.status != 'Approved':
            obj.status = 'Approved'
            obj.save()


@admin.action(description='Reject selected adoption requests')
def reject_requests(modeladmin, request, queryset):
    queryset.update(status='Rejected')


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'status', 'phone', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'pet__name', 'phone')
    readonly_fields = ('created_at', 'user', 'pet', 'phone', 'address', 'reason', 'previous_pet_experience', 'message')
    actions = [approve_requests, reject_requests]
    fieldsets = (
        ('Application', {
            'fields': ('user', 'pet', 'status')
        }),
        ('Contact', {
            'fields': ('phone', 'address')
        }),
        ('Details', {
            'fields': ('reason', 'previous_pet_experience', 'message')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
