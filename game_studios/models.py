from django.db import models
from django.urls import reverse


class Publisher(models.Model):
    """Game publisher model"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, editable=False, default='')
    image = models.ImageField(upload_to='game_studios/publishers_images', blank=True)

    def save(self, *args, **kwargs):
        bad_symbols = ['.', ',', ':', '!', '@', '?']
        result_slug = ''
        if not self.slug:
            for i in self.name:
                if i not in bad_symbols:
                    result_slug += i
            self.slug = result_slug.replace(' ', '_').lower()
        super(Publisher, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for each publisher"""
        return reverse('publisher', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Developer(models.Model):
    """Game developer model"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, editable=False, default='')
    image = models.ImageField(upload_to='game_studios/developers_images', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name.replace(' ', '_').lower()
        super(Developer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for each developer"""
        return reverse('developer', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
