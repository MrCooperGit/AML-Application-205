from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer, Director, Shareholder, Active_Session, UserProfile
# Register your models here.

admin.site.register(Customer)
admin.site.register(Director)
admin.site.register(Shareholder)
admin.site.register(Active_Session)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_staff', 'date_joined', 'user_profile_type')

    def user_profile_type(self, obj):
        return obj.userprofile.user_type

    user_profile_type.short_description = 'User Type'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type')


admin.site.register(UserProfile, UserProfileAdmin)
