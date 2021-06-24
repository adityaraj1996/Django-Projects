from django.db import models

# Create your models here.


class Operation(models.Model):
    sno = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=15)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operation}"
