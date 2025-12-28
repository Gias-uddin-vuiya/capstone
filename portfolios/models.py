from django.db import models
from django.utils.text import slugify
from django.utils import timezone

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

class Porject(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    cover_img = models.ImageField(
        upload_to='projects/',
        default='projects/default-project.png',
        blank=True
    )
    button_text = models.CharField(max_length=32)
    

    def __str__(self):
        return self.title

class Projects(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, null=True, blank=True)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.name

class Project_details(models.Model):

    project = models.OneToOneField(
        Projects,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="details"
    )

    p_name =  models.CharField(max_length=100)
    p_title = models.CharField(max_length=200)
    p_desc = models.TextField()

    p_goal_title = models.CharField(max_length=200, null=True, blank=True)
    p_goal_desc = models.TextField(null=True, blank=True)

    p_final_look_title = models.CharField(max_length=200, null=True, blank=True)
    p_final_look_desc = models.TextField(null=True, blank=True)

    p_conclusion_title = models.CharField(max_length=200, null=True, blank=True)
    p_conclusion_desc = models.TextField(null=True, blank=True)

    p_bibliography_title = models.CharField(max_length=200, null=True, blank=True)
    p_bibliography_desc = models.TextField(null=True, blank=True)

    # img field
    p_main_img = models.ImageField(upload_to="project_details_img/main/", null=True, blank=True)
    p_conclusion_img = models.ImageField(upload_to="project_details_img/conclusion/", null=True, blank=True)
    p_bibliography_img_1 = models.ImageField(upload_to="project_details_img/bibliography_1/", null=True, blank=True)
    p_bibliography_img_2 = models.ImageField(upload_to="project_details_img/bibliography_2/", null=True, blank=True)

    def __str__(self):
        return self.p_name

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project_details,
        on_delete=models.CASCADE,
        related_name="carousel_images"
    )

    image = models.ImageField(upload_to="project_details_img/carousel/", null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    

    order = models.PositiveIntegerField(default=0)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.project.p_name}-{self.title}-{self.order}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.project.p_name} - {self.title}"