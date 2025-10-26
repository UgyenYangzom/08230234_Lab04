from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    example_code = models.TextField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='journey_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    hobbies = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name