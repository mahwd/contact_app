from .models import Form
from django.contrib import admin


class formAdmin(admin.ModelAdmin):

    list_display = ['subject','message']
    list_filter = ['subject']
    search_fields = ['message']
    class Meta:
        model = Form

admin.site.register(Form,formAdmin)