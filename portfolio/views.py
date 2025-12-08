from django.shortcuts import render

def home(request):
    return render(request, "portfolio/home.html")

def about(request):
    return render(request, "portfolio/about.html")

def projects(request):
    return render(request, "portfolio/projects.html")

# portfolio/views.py
import requests
from django.shortcuts import render

def projects(request):
    # Your selected GitHub project names
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

    # Optional: Map custom images for each project
    project_images = {
        "my-django-app": "portfolio/images/project1.png",
        "portfolio-website": "portfolio/images/project2.png",
        "data-analysis-tool": "portfolio/images/project3.png",
    }

    for project in filtered_projects:
        project['image'] = project_images.get(project['name'], "portfolio/images/default_project.png")

    context = {
        "projects": filtered_projects
    }
    return render(request, "portfolio/projects.html", context)
