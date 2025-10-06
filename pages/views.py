from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Page, Banner, MenuLink

def home(request):
    homepage = Page.objects.filter(slug='home', is_published=True).first()
    today = timezone.now().date()
    banners = Banner.objects.filter(is_active=True).filter(
        date_end__isnull=True
    ) | Banner.objects.filter(is_active=True, date_end__gte=today)
    banners = banners.order_by('position')
    menu_links = MenuLink.objects.filter(is_visible=True).order_by('order')

    template = 'pages/page_detail.html' if homepage else 'pages/home.html'
    context = {
        'page': homepage,
        'banners': banners,
        'menu_links': menu_links,
    }
    return render(request, template, context)

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    banners = Banner.objects.filter(is_active=True).order_by('position')
    menu_links = MenuLink.objects.filter(is_visible=True).order_by('order')

    return render(request, 'pages/page_detail.html', {
        'page': page,
        'banners': banners,
        'menu_links': menu_links,
    })
