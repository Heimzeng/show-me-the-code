from django.contrib import admin
from .models import Article, Updates, Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','date','get_tags')
admin.site.register(Article,ArticleAdmin)
class UpdateAdmin(admin.ModelAdmin):
	list_display = ('title','date',)
admin.site.register(Updates,UpdateAdmin)
class TagAdmin(admin.ModelAdmin):
	list_display = ('name',)
admin.site.register(Tag,TagAdmin)