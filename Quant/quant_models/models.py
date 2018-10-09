from django.db import models
# Create your models here.


class Abnormal(models.Model):

    coin_up = models.IntegerField()
    coin_down = models.IntegerField()

    amplitude = models.FloatField()
    person = models.FloatField()
    flag = models.FloatField()

    status = models.BooleanField(default=True)

    create_time = models.DateTimeField(auto_now_add=True)

