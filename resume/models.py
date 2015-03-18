from django.db import models


class Fruit(models.Model):
    fruit_name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

    def __unicode__(self):
        return self.fruit_name