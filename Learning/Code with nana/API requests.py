import requests

respond = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = respond.json()
print(my_projects)
for project in my_projects:
    print(f"Project Name:{project['name']}\n Project Url:{project['web_url']}\n")
