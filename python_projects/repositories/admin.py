from django.contrib import admin

from .models import Repository
# Register your models here.
# admin.site.register(Repository)
@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    ordering = ['-number_of_stars']
