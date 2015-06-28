from django.db import models


class Rating(models.Model):
    grade = models.FloatField()
    nr_of_people = models.IntegerField()

    def printrating(self):
        return self.grade


    def getrating(self, new_grade):
        self.nr_of_people = self.nr_of_people + 1
        new_rating = (self.grade * (self.nr_of_people - 1) + new_grade) / self.nr_of_people
        self.grade = new_rating
        return new_rating


class Movie(models.Model):
    title = models.CharField(max_length = 100)
    launch_date = models.IntegerField()
    imdb_link = models.CharField(max_length = 100)
    poster = models.CharField(max_length = 1000,default='https://nanohub.org/groups/bnc/Image:/equipment/missing_equip.gif') #I'll add the link to the photo 
    grade = models.ForeignKey('Rating',default = '0')

    def __str__(self):
        return self.title
