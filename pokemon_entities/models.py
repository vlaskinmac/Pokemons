from django.db import models


class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Имя')
    title_en = models.CharField(max_length=200, default='', blank=True, verbose_name='имя на английском языке')
    title_jp = models.CharField(max_length=200, default='', blank=True, verbose_name='имя на японском языке')
    image = models.ImageField(blank=True, upload_to='pokemons', verbose_name='Фотка')
    description = models.TextField(blank=True, default='', verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        'self', related_name='next_evolution',
        verbose_name='из кого эволюционировал',
        on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='entities', on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Появится')
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Исчезнет')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strendth = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')
