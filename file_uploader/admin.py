from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "image", ]
    list_filter = ["title", "image"]


admin.site.register(Image)
