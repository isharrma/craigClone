from django.db import models


class Search(models.Model):
    search = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now=True)
    #auro_now= True saves the time of created automatically,can be used for last searched or last updated.
    def __str__(self):
        return '{}'.format(self.search)