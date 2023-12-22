from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=50)
    review_text = models.TextField()
    review_date = models.DateField()

    def __str__(self):
        return f"{self.movie.name} - {self.reviewer_name}"

