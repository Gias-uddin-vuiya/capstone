from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_img = models.ImageField(upload_to='profiles/')
    profile_bg_img = models.ImageField(upload_to='profiles/backgrounds/')
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    about = models.TextField()
    icons = models.JSONField()  # Store social media icons and links as JSON

    def __str__(self):
        return self.name