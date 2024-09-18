from django.contrib import admin

from server.presentations.models import Presentation, Creator


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = (
        "title", "creator", "thumbnail"
    )
    search_fields = ("title", "creator__name")


@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = (
        "name", "profile_url"
    )
    search_fields = ("name",)
