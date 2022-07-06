from django.shortcuts import render, redirect
import requests
from .models import Repository
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from time import sleep
from django.conf import settings

def get_repo_data():
    results = []
    # ASYNC REQUIRED FOR ALL 10 PAGES:
    page = 1
    URL = f'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&per_page=100&page={page}'
    data = requests.get(URL).json()
    if 'items' in data:
        for repo in data['items']:
            result = {}
            result['repo_id'] = repo['id']
            result['name'] = repo['name']
            result['url'] = repo['html_url']
            result['created_date'] = repo['created_at']
            result['last_push_date'] = repo['pushed_at']
            result['description'] = repo['description']
            result['number_of_stars'] = repo['stargazers_count']
            results.append(result)
    return results



def save_repo_data():
    repos = get_repo_data()

    for repo in repos:
        if not Repository.objects.filter(repo_id = repo['repo_id']).exists():
            print(f"NEW REPO {repo['name']}")
            repository= Repository.objects.create(repo_id=repo['repo_id'])
            repository.name = repo['name']
            repository.url = repo['url']
            repo['created_date'].replace('T', ' ')
            repo['created_date'].replace('Z', '')
            repository.created_date = repo['created_date']
            repository.last_push_date = repo['last_push_date']
            repository.description = repo['description']
            repository.number_of_stars = repo['number_of_stars']
            repository.save()
        else:
            print(f"UPDATING REPO {repo['name']}")
            repository = Repository.objects.get( repo_id = repo['repo_id'])
            repository.name = repo['name']
            repository.url = repo['url']
            repo['created_date'].replace('T', ' ')
            repo['created_date'].replace('Z', '')
            repository.created_date = repo['created_date']
            repository.last_push_date = repo['last_push_date']
            repository.description = repo['description']
            repository.number_of_stars = repo['number_of_stars']
            repository.save()


class RepositoryDetailView(DetailView):

    model = Repository

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class RepositoryListView(ListView):

    model = Repository
    paginate_by = settings.GITHUB_REPOSITORY_RESULTS_PER_PAGE  # if pagination is desired
    ordering = ['-number_of_stars']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get(self, request, *args, **kwargs):
        # if on first load: grab and save data from github API
        page_number = request.GET.get('page')
        if not page_number:
            save_repo_data()
        # if no repos in the DB: grab and save data from github API
        if Repository.objects.all().count() == 0:
            save_repo_data()


        return super().get(request, *args, **kwargs)
