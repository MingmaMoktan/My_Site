from django.shortcuts import render
import requests

def home(request):
    return render(request, "portfolio/home.html")

def about(request):
    return render(request, "portfolio/about.html")

def projects(request):
    return render(request, "portfolio/projects.html")

def projects(request):
    selected_projects = [
        "Spotify_clone",
        "ETL_Project_1",
        "Automated_backup_script"
    ]

    github_username = "MingmaMoktan"
    github_api_url = f"https://api.github.com/users/{github_username}/repos"

    try:
        response = requests.get(github_api_url)
        response.raise_for_status()
        repos = response.json()
    except requests.RequestException:
        repos = []

    # Filter only the selected projects
    filtered_projects = [repo for repo in repos if repo['name'] in selected_projects]

    context = {
        "projects": filtered_projects
    }
    return render(request, "portfolio/projects.html", context)
