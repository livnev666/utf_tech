from django.contrib import admin
from .models import Food, FoodCategory

# Register your models here.


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'internal_code', 'code', 'name_ru', 'description_ru',
                    'description_en', 'description_ch', 'is_vegan', 'is_special',
                    'cost', 'category']
    list_display_links = ['name_ru']
    filter_horizontal = ['additional']
    ordering = ['id']


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ru', 'name_en', 'name_ch', 'order_id']
    list_display_links = ['name_ru']
    ordering = ['id']

