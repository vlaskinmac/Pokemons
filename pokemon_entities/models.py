from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


