from django.db import models

# Create your models here.
class Card(models.Model):
    definition = models.CharField(max_length=200)
    concept = models.CharField(max_length=20)
    topic = models.CharField(max_length=20)

    def __str__(self):
        return self.definition