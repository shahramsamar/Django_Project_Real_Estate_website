from django.contrib import admin
from blog.models import Category, Post, Comment
# Register your models here.

from blog.models import Newsletter

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author', 'counted_views', 'status', 
                   'login_required', 'published_date', 'created_date')
    list_filter = ['status','author']
    search_fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display =('name', 'post','approved', 'created_date' )
    list_filter = ('post', 'approved')
    search_fields = ['name','post']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Newsletter)
admin.site.register(Comment, CommentAdmin)

