from django.contrib import admin

from .models import State, PaymentType, Organization, FuelType, FuelColumn, FuelStorage, Fuel, FuelPrice, FuelColumnPointer, User, UserTypes


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('title', )
    search_fields = ('title', 'attr')
    list_per_page = 20


class FeulTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'attr')
    list_per_page = 20


admin.site.register(State)
admin.site.register(PaymentType)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(FuelType, FeulTypeAdmin)
admin.site.register(FuelColumn)
admin.site.register(FuelStorage)
admin.site.register(Fuel)
admin.site.register(FuelPrice)
admin.site.register(FuelColumnPointer)
admin.site.register(User)
admin.site.register(UserTypes)