from django.contrib import admin
from .models import Page, Banner, MenuLink

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published',)
    search_fields = ('title', 'content')
    date_hierarchy = 'updated_at'

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'is_active', 'date_end')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    ordering = ('position',)

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'is_visible')
    list_editable = ('url', 'order', 'is_visible')
    list_filter = ('is_visible',)

admin.site.site_header = "EWIK Administration"
admin.site.site_title = "EWIK Admin Portal"
admin.site.index_title = "Welcome to EWIK Content Management"
