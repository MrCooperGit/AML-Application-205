from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer, CustomUser, Company, Director, Shareholder, Active_Session, UserProfile, Entity, AvailableApps, Active_Session
from risk_assessment.models import RiskAssessment
from landing_app.models import UserTab


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_staff', 'date_joined', 'user_profile_type')

    def user_profile_type(self, obj):
        return obj.userprofile.user_type

    user_profile_type.short_description = 'User Type'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class RiskAssessmentInline(admin.TabularInline):
    model = RiskAssessment
    extra = 0
    list_display = ['offer_anonymity', 'offer_large_value_services', 'offer_services_black_list', 'offer_services_grey_list',
                    'offer_services_outside_NZ', 'cash_intensive', 'company_services', 'trust_services', 'remittance_services', 'virtual_assets_services']


class CustomerInline(admin.TabularInline):
    model = Customer
    extra = 0


class CustomUserInline(admin.TabularInline):
    model = CustomUser
    extra = 0
    fields = ('email', 'first_name', 'last_name',)
    list_display = ('email', 'first_name', 'last_name',)
    exclude = ('password', 'groups', 'user_permissions')


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


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('users',)
    list_per_page = 20
    inlines = [RiskAssessmentInline, CompanyInline, DirectorInline,
               ShareholderInline, CustomUserInline, UserProfileInline, CustomerInline]
