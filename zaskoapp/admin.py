from django.contrib import admin

from zaskoapp.models import BookingRequest, Contact, NewsLetter

# Register your models here.
admin.site.register(Contact)
admin.site.register(NewsLetter)


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'service',
        'preferred_date',
        'preferred_time',
        'preferred_contact',
        'status',
        'created_at',
    )
    list_filter = ('status', 'service', 'preferred_contact', 'created_at')
    search_fields = ('name', 'company', 'email', 'phone', 'service', 'project_type', 'message')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)
    ordering = ('-created_at',)
