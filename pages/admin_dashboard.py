from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from pages.models import Page, Banner, MenuLink
from django.urls import reverse
from django.contrib.auth.models import User, Group
from pages.admin import PageAdmin, BannerAdmin, MenuLinkAdmin
from django.contrib.auth.admin import UserAdmin



class EwikAdminSite(admin.AdminSite):
    site_header = "EWIK Administration"
    site_title = "EWIK Admin Portal"
    index_title = "Welcome to EWIK Content Management"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='ewik-dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        context = dict(
    self.each_context(request),
    page_count=Page.objects.count(),
    banner_count=Banner.objects.count(),
    menu_count=MenuLink.objects.count(),
    page_add_url=reverse('admin:pages_page_add', current_app=self.name),
    banner_add_url=reverse('admin:pages_banner_add', current_app=self.name),
    menulink_add_url=reverse('admin:pages_menulink_add', current_app=self.name),
)


        return TemplateResponse(request, "admin/dashboard.html", context)

admin_site = EwikAdminSite(name='ewik_admin')
admin_site.register(Page, PageAdmin)
admin_site.register(Banner, BannerAdmin)
admin_site.register(MenuLink, MenuLinkAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group)

