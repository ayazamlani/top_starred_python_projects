from django.db import models

# Create your models here.
class Repository(models.Model):
    repo_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    url = models.URLField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    last_push_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    number_of_stars = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "repositories"

    def __str__(self):
        return self.name
