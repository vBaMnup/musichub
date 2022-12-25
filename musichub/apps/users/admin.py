from django.contrib import admin

from .models import AuthUser, SocialLinks


@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'display_name', 'join_date')
    list_display_links = ('email', )


@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('user', 'link')
