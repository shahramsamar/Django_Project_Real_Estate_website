from django.contrib import admin
from blog.models import Category, Post
# Register your models here.

from blog.models import Newsletter

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status', 
                   'login_required', 'published_date', 'created_date')
    list_filter = ['status']
    search_fields = ['title', 'content']




admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Newsletter)

