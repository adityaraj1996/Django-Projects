from django.db import models

# superuser - adtya, pwd - Ariyank1

# Create your models here.

class UrlData(models.Model):
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"
