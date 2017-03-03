from django.contrib import admin
from .models import Company, Position, Category

# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company_website",
                    "offer_website", "position", "category")


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
