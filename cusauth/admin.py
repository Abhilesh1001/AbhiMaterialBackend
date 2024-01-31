from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, ProfileUpdate

class UserAdmin(BaseUserAdmin):
    list_display = ["id", "email", "name", "tc", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "tc"]}),
        ("Permissions", {"fields": ["is_admin", "groups", "user_permissions"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "tc", "password1", "password2", "groups", "user_permissions"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = ["groups", "user_permissions"]

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)

@admin.register(ProfileUpdate)
class AdminProfileUpdate(admin.ModelAdmin):
    list_display = ['user', 'Date_of_Birth', 'profile_picture', 'pan_number', 'pan_picture']
