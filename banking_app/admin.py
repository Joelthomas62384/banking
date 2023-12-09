from django.contrib import admin
from . models import *

# Register your models here.
class SubBranchInline(admin.TabularInline):
    model = Sub_Branches
    extra = 1  # Number of empty forms to display for adding new related Sub_Branches

class BranchesAdmin(admin.ModelAdmin):
    inlines = [SubBranchInline]

class MaterialInline(admin.TabularInline):
    model = Material
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [MaterialInline]

admin.site.register(Branches, BranchesAdmin)
admin.site.register(UserProfile,UserProfileAdmin)