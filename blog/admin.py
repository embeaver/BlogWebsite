from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# Add models to the admin site
# https://djangocentral.com/building-a-blog-application-with-django/

# Customize the way the post information is displayed in the admin site - more info
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

# Add this Post model to the admin site
admin.site.register(Post, PostAdmin)

# Add comment posts to admin site
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

# Add comment model to admin site
admin.site.register(Comment, CommentAdmin)