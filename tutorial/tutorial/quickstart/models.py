from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now=False)
    director = models.CharField(max_length=50)
    user_score = models.FloatField(default=0)

    def __str__(self):
        return "title : {}".format(self.title)