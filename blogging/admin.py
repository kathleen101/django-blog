from django.contrib import admin
from blogging.models import Post, Category


class MembershipInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)