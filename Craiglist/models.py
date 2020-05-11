from django.db import models


class Search(models.Model):
    search = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now=True)
    #auro_now= True saves the time of created automatically,can be used for last searched or last updated.
    def __str__(self):
        return '{}'.format(self.search)

    # Meta class is used to give meta(extra) info about the model/database like ordering i.e order by and verbose is for simple naming
    class Meta:
        verbose_name_plural = "Searches"