from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    phone = models.CharField(max_length=20)
    otc = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    #username = None
    #password = None
    def __str__(self):
        return '{}'.format(self.username + " " + self.email)


class Pereval(models.Model):
    STATUS_CHOICES = (
        ('NEW', 'New'),
        ('PND', 'Pending'),
        ('ACPT', 'Accepted'),
        ('RJCT', 'Rejected'),
    )
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='NEW')
    beauty_title = models.CharField(max_length=5)
    title = models.CharField(max_length=30, blank=True, unique=True)
    other_titles = models.CharField(max_length=30, blank=True)
    connect = models.CharField(max_length=50, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    lofitude = models.FloatField(blank=True)
    logitude = models.FloatField(blank=True)
    height = models.FloatField(blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Level(models.Model):
    SEASON_CHOICES = (
        ('WIN', 'Winter'),
        ('SUM', 'Summer'),
        ('OUT', 'Outhemn'),
        ('SPR', 'Spring'),
    )
    season = models.CharField(max_length=5, choices=SEASON_CHOICES)
    level = models.CharField(max_length=5, blank=True, null=True)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='levels')

    def __str__(self):
        return '{}'.format(self.season + " " + self.level)


class Images(models.Model):
    data = models.ImageField(upload_to='images/%Y-%m-%d/')
    title = models.CharField(max_length=125)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='img')


