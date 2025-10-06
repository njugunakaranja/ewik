from django.db import models
from django.utils import timezone

# === Navigation Menu ===
class MenuLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True)
    page = models.ForeignKey('Page', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


# === Page Content ===
class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# === Homepage Banners ===
class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True)
    button_text = models.CharField(max_length=50, blank=True, default="Learn More")
    position = models.PositiveIntegerField(default=0)
    start_date = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def is_current(self):
        today = timezone.now().date()
        if self.start_date and self.start_date > today:
            return False
        if self.date_end and self.date_end < today:
            return False
        return self.is_active

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['position']
