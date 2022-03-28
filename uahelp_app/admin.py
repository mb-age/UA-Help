from django.contrib import admin
from . import models


# Register your models here.

class ProfileLinkInlineAdmin(admin.TabularInline):
    model = models.Link
    extra = 1



@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'account_type')
    # fieldsets = (
    #     ("Informacje podstawowe", {
    #         'fields': ('name', 'user')
    #     }),
    #     ("Inne", {
    #         'fields': ('account_type', 'country')
    #     }),
    # )
    ordering = ('-id',)
    inlines = (ProfileLinkInlineAdmin,)


@admin.register(models.AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    ordering = ('type',)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'content')


@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'content')
    ordering = ('profile',)


# @admin.register(models.Country)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     ordering = ('name',)




