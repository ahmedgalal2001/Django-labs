from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cast(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CommonInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    categories = models.ManyToManyField(Category)
    casts = models.ManyToManyField(Cast)
    poster_image = models.ImageField(upload_to='posters/')

    class Meta:
        abstract = True

class Movie(CommonInfo):
    pass

class Series(CommonInfo):
    pass

