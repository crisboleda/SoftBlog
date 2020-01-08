from django.contrib import admin
from posts.models import Post, Caterory, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'category', 'get_tags', 'author', 'data_published')
    readonly_fields = ('data_published',)

    def get_tags(self, obj):
        return ", ".join([tag.name_tag for tag in obj.tags.all().order_by('name_tag')])

@admin.register(Caterory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category', 'created')
    readonly_fields = ('created',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name_tag', 'created')
    readonly_fields = ('created',)

