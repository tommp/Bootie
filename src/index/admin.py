from django.contrib import admin
from index.models import FrontpageContext


class FrontpageContextAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'top_logo']}),
    ]


admin.site.register(FrontpageContext, FrontpageContextAdmin)
