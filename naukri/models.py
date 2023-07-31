from django.db import models

# Create your models here.
class Desc(models.Model):
    droll = models.CharField(max_length = 50)
    rating = models.FloatField()
    review = models.IntegerField()
    day = models.IntegerField(default = 1)
    yrs = models.CharField(max_length = 20)
    mony = models.CharField(max_length = 20)
    loction = models.CharField(max_length = 50)
    about = models.CharField(max_length = 500)

    def __str__(self):
            return f'droll is :- {self.droll}, rating is :- {self.rating}, review is :-{self.review}, yrs is :- {self.yrs}, mony is :- {self.mony}, loction is :- {self.loction}, about is :- {self.about}, day is :- {self.day}'