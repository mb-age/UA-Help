from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'account_type', 'user', 'country')
    fieldsets = (
        ("Informacje podstawowe", {
            'fields': ('name', 'user')
        }),
        ("Pierdoły", {
            'fields': ('account_type', 'country')
        }),
    )
    ordering = ('-name',)


admin.site.register(models.AccountType)
admin.site.register(models.Post)
admin.site.register(models.Link)
admin.site.register(models.Country)




