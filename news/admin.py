from django.contrib import admin
from .models import Article,Tag,Editor

#Register models
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


# Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Editor)