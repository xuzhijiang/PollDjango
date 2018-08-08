from django.contrib import admin
from .models import OAuthUser, OAuthConfig


class OAuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'nikename', 'type', 'picture', 'email',)
    list_display_links = ('id', 'nikename')
    list_filter = ('author', 'type',)


class OAuthConfigAdmin(admin.ModelAdmin):
    list_display = ('type', 'appkey', 'appsecret', 'is_enable')
    list_filter = ('type',)
