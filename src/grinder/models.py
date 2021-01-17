from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    URLField,
    JSONField,
)
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from track.models import Track
from playlist.models import Playlist


class Tag(Model):
    """Labels to help categorize data"""

    name = CharField(max_length=31, unique=True)
    slug = AutoSlugField(
        help_text="A label for URL config.",
        max_length=31,
        populate_from=["name"],
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return URL to detail page of Tag"""
        return reverse(
            "tag_detail", kwargs={"slug": self.slug}
        )

    def get_update_url(self):
        """Return URL to update page of Tag"""
        return reverse(
            "tag_update", kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        """Return URL to delete page of Tag"""
        return reverse(
            "tag_delete", kwargs={"slug": self.slug}
        )

class Grinde(Model):
    """Grindes that happened on data"""

    name = CharField(max_length=31, unique=True)
    slug = AutoSlugField(
        help_text="A label for URL config.",
        max_length=31,
        populate_from=["name"],
    )
    analysis = JSONField(null=True)
    tracks = ManyToManyField(Track)
    playlists = ManyToManyField(Playlists)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return URL to detail page of Grinde"""
        return reverse(
            "tag_detail", kwargs={"slug": self.slug}
        )

    def get_update_url(self):
        """Return URL to update page of Grinde"""
        return reverse(
            "tag_update", kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        """Return URL to delete page of Grinde"""
        return reverse(
            "tag_delete", kwargs={"slug": self.slug}
        )
