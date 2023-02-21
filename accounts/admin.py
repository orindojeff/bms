from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.db.models import Count
from django.utils.translation import ngettext

from accounts.forms import RegistrationForm, UserAdminChangeForm
from accounts.models import Profile, Message
from admin.admin import spm_admin_site
from accounts.mixins import ExportCsvMixin

User = get_user_model()

admin.site.site_header = "WALLPAPER KENYA ADMIN"
admin.site.site_title = "Wallpaper Kenya Admin Portal"
admin.site.index_title = "Welcome to Wallpaper Kenya Admin Portal"

# admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(ExportCsvMixin, BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = RegistrationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'email', 'username', 'user_type')
    search_fields = ('name', 'email', 'username',)
    list_filter = ('is_active', 'is_archived', 'updated', 'created', 'user_type')
    actions = ['make_active', 'make_inactive', 'export_as_csv']
    readonly_fields = ['created', 'updated']

    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('name', 'email', 'username')}),
        ('Permissions', {'fields': ('user_type',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'username', 'user_type', 'password1', 'password2')}
         ),
    )
    ordering = ['email']
    filter_horizontal = ()

    def make_active(self, request, queryset):
        updated = queryset.update(is_active=True, is_archived=False)
        self.message_user(request, ngettext(
            '%d User has successfully been marked as active.',
            '%d Users have been successfully marked as active.',
            updated,
        ) % updated, messages.SUCCESS)

    make_active.short_description = "Activate User"

    def make_inactive(self, request, queryset):
        updated = queryset.update(is_archived=True, is_active=False)
        self.message_user(request, ngettext(
            '%d User has been archived successfully.',
            '%d Users have been archived successfully.',
            updated,
        ) % updated, messages.INFO)

    make_inactive.short_description = "Archive User"


@admin.register(Profile)
class ProfileAdmin(ExportCsvMixin, ModelAdmin):
    search_fields = ['user__name']
    list_display = ['phone_number', 'photo', 'gender']
    list_display_links = ['phone_number']
    search_help_text = "Search by name"
    list_filter = ('gender', 'updated', 'created')
    actions = ['export_as_csv']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Message)
class MessagesAdmin(ExportCsvMixin, ModelAdmin):
    search_fields = ['subject', 'name', 'message']
    list_display = ['subject', 'message', 'name', 'email']
    list_display_links = ['subject']
    search_help_text = "Search by subject or message or sender"
    list_filter = ('is_read', 'updated', 'created')
    actions = ['mark_as_read', 'export_as_csv']

    def make_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, ngettext(
            '%d Message status has been updated successfully.',
            '%d Messages status has been updated successfully.',
            updated,
        ) % updated, messages.SUCCESS)

    make_as_read.short_description = "Mark as read"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


spm_admin_site.register(Message, MessagesAdmin)