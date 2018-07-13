from django.contrib import admin

# Register your models here.

from .models import Tag, Article, Category


class TagAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('title', 'category', 'author', 'date_time', 'view',)
    list_filter = ('category', 'author',)
    filter_horizontal = ('tag',)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
