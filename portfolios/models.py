from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_img = models.ImageField(
        upload_to='profiles/',
        default='profiles/default-profile.png',
        blank=True
    )

    profile_bg_img = models.ImageField(
        upload_to='profiles/backgrounds/',
        default='profiles/backgrounds/default-bg.png',
        blank=True
    )


    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    about = models.TextField()
    icons = models.JSONField()  # Store social media icons and links as JSON

    def __str__(self):
        return self.name