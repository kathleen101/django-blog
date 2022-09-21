from django.contrib import admin
from blogging.models import Post, Category


class MembershipInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
