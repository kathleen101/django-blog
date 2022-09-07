from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]


class PostAdmin(admin.ModelAdmin):
    fields = (Post.title, Post.text, Post.author, Post.created_date, Post.modified_date, Post.published_date)


class CategoryAdmin(admin.ModelAdmin):
    fields = (Category.name, Category.description)


class CategoryAdmin(admin.ModelAdmin):
    exclude = (Category.posts,)


admin.site.register(Post, PostAdmin)
