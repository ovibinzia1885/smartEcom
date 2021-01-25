from django.contrib import admin
from .models import Setting,ContactMessage,FAQ

admin.site.register(Setting)
admin.site.register(ContactMessage)

class FAQamin(admin.ModelAdmin):
    list_display = ['ordernumber', 'question', 'status', 'created_at', 'updated_at']


admin.site.register(FAQ, FAQamin)
