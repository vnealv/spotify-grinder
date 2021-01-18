from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    IntegerField,
    URLField,
)
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from grinder.models import Tag

class Track (Model):
    spotify_id = CharField(max_length=40, unique=True)
    name = (max_length=44, unique=True)
    href = URLField(
        max_length=255  # https://tools.ietf.org/html/rfc3986
    )
    hash_check = CharField(blank=True, default=None, max_length=32, editable=True, null=True)
    tags = ManyToManyField(Tag)

    slug = AutoSlugField(
        help_text="A label for URL config.",
        max_length=40,
        populate_from=["spotify_id"],
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return URL to detail page of Track"""
        return reverse(
            "track_detail", kwargs={"slug": self.slug}
        )

    def get_update_url(self):
        """Return URL to update page of Track"""
        return reverse(
            "track_update", kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        """Return URL to delete page of Track"""
        return reverse(
            "track_delete", kwargs={"slug": self.slug}
        )
