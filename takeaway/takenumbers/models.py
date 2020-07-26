from django.db import models

# Create your models here.

class Bestellnummer(models.Model):
    bnum = models.CharField(max_length=10,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)
    archieved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.bnum)