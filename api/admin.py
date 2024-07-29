from django.contrib import admin
from .models import User, Expense

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'mobile_number')
    search_fields = ('email', 'name')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'description', 'amount', 'split_type')
    search_fields = ('description',)
    list_filter = ('split_type',)
