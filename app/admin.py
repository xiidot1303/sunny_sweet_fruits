from django.contrib import admin
from app.models import *

class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('title_ru', 'title_en', 'photo')
    list_display_links = ('photo',)
    list_editable = ('title_ru', 'title_en')
    search_fields = ['title_ru', 'title_en']
    # list_filter = ('title_uz', 'title_ru')


class SubCategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('title_ru', 'title_en', 'category')
    list_display_links = ('category', )
    list_editable = ('title_ru', 'title_en')
    search_fields = ['title_ru', 'title_en']
    
    list_filter = ['category']

    # fieldsets = [
    #     (None, {'fields': ['title_uz', 'title_ru']}),
    #     ('Image', {'fields': ['category']}),

    # ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'sub_category', 'grade', 'drying_type', 'photo']

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)