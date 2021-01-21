from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    imgUrl = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title