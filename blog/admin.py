from django.contrib import admin

from .models import Post,Category, Comment

class CommentItemInLine(admin.TabularInline): #To show the comments in the posts editing body session
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','intro','body'] #inputting the admin search feature  !!!!!   Do not use foreign key !!!
    list_display = ['title','slug', 'category','created_at', 'status'] #setting the details to be shown for each post in the admin area
    list_filter = ['category', 'created_at', 'status'] # sets up attributes to filter the post display
    inlines = [CommentItemInLine]
    prepopulated_fields = {'slug': ('title',)} #Automatically generates the slug input
    
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)} #Automatically generates the slug input
    
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name'] 
    list_display = ['name', 'post', 'created_at']
    
    
# Register your models here.
admin.site.register(Post, PostAdmin) #note that the 'PostAdmin' has been added to register
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)