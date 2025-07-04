from django.db import models


class AtelierEntity(models.Model):
    TYPES_CHOICES = (
        ('PR', 'Фурнитура'),
        ('SR', 'Услуга'),
    )

    name = models.CharField(max_length=100)
    price = models.FloatField()
    type = models.CharField(max_length=20, choices=TYPES_CHOICES)
    available = models.BooleanField(default=True)
    description = models.TextField(default='', blank=True)
    image_path = models.CharField(max_length=100, default='default.png')

    def __str__(self):
        return self.name
