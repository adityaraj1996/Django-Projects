from django.db import models

# superuser = admin ,test123

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return f"{self.name}"
