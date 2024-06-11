from django.db import models
import jsonfield

from products.translate import from_cyrillic_to_latin


def default_urls():
    return {'stopgame': ""}


class Article(models.Model):
    """News article model"""
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    short_description = models.CharField(max_length=200, blank=True)
    image = models.TextField()
    tags = models.ManyToManyField('Tag', verbose_name='Tags', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', editable=False)

    def save(self, *args, **kwargs):
        """Auto set slug field as article name"""
        if not self.slug:
            self.slug = from_cyrillic_to_latin(str(self.title))
        super(Article, self).save(*args, **kwargs)


class Tag(models.Model):
    """News article tags model"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, editable=False)

    def save(self, *args, **kwargs):
        """Auto set slug field as article tag name"""
        if not self.slug:
            self.slug = from_cyrillic_to_latin(str(self.name))
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Error(models.Model):
    """Parsing error model"""
    timestamp = models.DateField(auto_now_add=True)
    data = jsonfield.JSONField()


class Url(models.Model):
    """Article tag url model"""
    tags = models.ManyToManyField('Tag', verbose_name='Tags', blank=True)
    url_data = jsonfield.JSONField(default=default_urls)

