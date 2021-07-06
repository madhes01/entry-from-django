from django.db import models


class Entry(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    file= models.FileField()
    class Meta:
            db_table = "Entry"








