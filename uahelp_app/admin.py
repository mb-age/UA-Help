from django.contrib import admin
from . import models


# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.AccountType)
admin.site.register(models.Post)
admin.site.register(models.Link)
admin.site.register(models.Country)



