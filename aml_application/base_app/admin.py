from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer, CustomUser, Company, Director, Shareholder, Active_Session, UserProfile, Entity
from risk_assessment.models import RiskAssessment
# Register your models here.


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


class CustomerInline(admin.TabularInline):
    model = Customer
    extra = 0


class UserProfileInline(admin.TabularInline):
    list_display = ('user', 'user_type')
    model = UserProfile
    extra = 0


class CustomUserInline(admin.TabularInline):
    list_display = ('email', 'first_name', 'last_name', 'entity')
    model = CustomUser
    extra = 0


class CompanyInline(admin.TabularInline):
    list_display = ('name', 'company_registration_num', 'address')
    exclude = ('password', 'groups', 'user_permissions')
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
    inlines = [RiskAssessmentInline, CompanyInline, DirectorInline,
               ShareholderInline, ActiveSessionInline, UserProfileInline, CustomUserInline, CustomerInline]
