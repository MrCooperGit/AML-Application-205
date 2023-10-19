from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer, Company, Director, Shareholder, UserProfile, Entity, AvailableApps, Active_Session
from landing_app.models import UserTab
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_staff', 'date_joined', 'user_profile_type')

    def user_profile_type(self, obj):
        return obj.userprofile.user_type

    user_profile_type.short_description = 'User Type'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class CustomerInline(admin.TabularInline):
    model = Customer
    extra = 0


class UserProfileInline(admin.TabularInline):
    list_display = ('user', 'user_type')
    model = UserProfile
    extra = 0


class CompanyInline(admin.TabularInline):
    list_display = ('name', 'company_registration_num', 'address')
    model = Company
    extra = 0


class DirectorInline(admin.TabularInline):
    model = Director
    extra = 0


class ShareholderInline(admin.TabularInline):
    model = Shareholder
    extra = 0


class ActiveSessionInline(admin.TabularInline):
    model = Active_Session
    extra = 0


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('users',)
    list_per_page = 20
    inlines = [CompanyInline, DirectorInline,
               ShareholderInline, ActiveSessionInline, UserProfileInline, CustomerInline]

@admin.register(AvailableApps)
class AvailableAppsAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name')
    list_per_page = 20


@admin.register(UserTab)
class UserTabAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'app_id', 'is_active')
    list_per_page = 20