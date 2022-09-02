from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    phone = models.CharField(max_length=20)
    otc = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user.username
        #return '{}'.format(self.user.first_name + " " + self.otc + " " + self.user.last_name)

class Level(models.Model):
     season = models.CharField(max_length=5, choices=(('win', 'Winter'),
                                                      ('sum', 'Summer'),
                                                      ('out', 'Outhemn'),
                                                      ('spr', 'Spring'),
                                                      ),
                               default='win'
                               )
     level = models.CharField(max_length=5, blank=True)
     #pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='levels')


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
    add_time = models.DateField(auto_now_add=True)
    lofitude = models.FloatField(blank=True)
    logitude = models.FloatField(blank=True)
    height = models.FloatField(blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    #level = models.ForeignKey(Level, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Images(models.Model):
    img = models.ImageField("Изображение", upload_to='uploads/')
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)

