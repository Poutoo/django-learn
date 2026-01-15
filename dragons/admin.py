from django.contrib import admin
from django.utils.html import format_html
from .models import Dragon

@admin.register(Dragon)
class DragonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'image_tag')
    list_filter = ('categorie',)
    search_fields = ('nom', 'description')

    def image_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.photo.url)
        return "-"
    image_tag.short_description = 'Image'
