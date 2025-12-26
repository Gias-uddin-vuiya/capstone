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

    p_goal_title = models.CharField(max_length=200)
    p_goal_desc = models.TextField()

    p_final_look_title = models.CharField(max_length=200)
    p_final_look_desc = models.TextField()

    p_conclusion_title = models.CharField(max_length=200)
    p_conclusion_desc = models.TextField()

    p_bibliography_title = models.CharField(max_length=200)
    p_bibliography_desc = models.TextField()

    # img field
    p_main_img = models.ImageField(upload_to="project_details_img/main/")
    p_conclusion_img = models.ImageField(upload_to="project_details_img/conclusion/")
    p_bibliography_img_1 = models.ImageField(upload_to="project_details_img/bibliography_1/")
    p_bibliography_img_2 = models.ImageField(upload_to="project_details_img/bibliography_2/")

    def __str__(self):
        return self.p_name
