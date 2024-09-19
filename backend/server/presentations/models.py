from django.db import models
from django.utils.translation import gettext as _

from server.base.models import BaseModel


class Creator(BaseModel):
    name = models.CharField(max_length=100, null=False, verbose_name=_("Name"))
    profile_url = models.URLField(max_length=100, null=True, blank=True, verbose_name=_("Profile URL"))

    class Meta:
        verbose_name = _("Creator")
        verbose_name_plural = _("Creators")


class Presentation(BaseModel):
    title = models.CharField(max_length=100, null=False, verbose_name=_("Name"), db_index=True)
    thumbnail = models.URLField(max_length=100, null=True, blank=True, verbose_name=_("Thumbnail"))
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Presentation")
        verbose_name_plural = _("Presentations")
        ordering = ["created_at"]
