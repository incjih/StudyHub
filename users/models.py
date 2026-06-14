from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    university = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    study_style = models.CharField(max_length=50, choices=[
        ('visual', 'Visual'),
        ('reading', 'Reading/Writing'),
        ('auditory', 'Auditory'),
        ('kinesthetic', 'Kinesthetic'),
    ], blank=True)
    subjects = models.ManyToManyField('groups.Subject', blank=True)
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def update_rating(self, new_score):
        total = self.rating * self.rating_count + new_score
        self.rating_count += 1
        self.rating = total / self.rating_count
        self.save()
