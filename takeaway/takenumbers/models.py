from django.db import models

# Create your models here.

class Bestellnummer(models.Model):
    bnum = models.IntegerField(unique=True,default=1)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)
    archieved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.bnum)