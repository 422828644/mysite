from django.db import models

# Create your models here.
# Table name
db_table = 'sys'


# 人
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    first_name = models.CharField("姓", max_length=30)
    last_name = models.CharField("名", max_length=30)
    shirt_size = models.CharField("T恤的size", max_length=1, choices=SHIRT_SIZES)


# 音乐家
class Musician(models.Model):
    first_name = models.CharField("姓", max_length=50)
    last_name = models.CharField("名", max_length=50)
    instrument = models.CharField("主乐器", max_length=100)


# 专辑
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField("专辑名", max_length=100)
    release_date = models.DateField("发布日期")
    num_starts = models.IntegerField()


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField("名称", max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)


class Fruit(models.Model):
    name = models.CharField("名称", max_length=100, primary_key=True)


class Manufacturer(models.Model):
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
