import requests
import sqlite3

respond = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = respond.json()

conn = sqlite3.connect('sql_url.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Projects
            (Project TEXT, Project_Url Url)''')
# cur.execute('''
#             ALTER TABLE Projects
            # DROP Name''')
# cur.execute('''ALTER TABLE Projects
#             ADD Path TEXT''')

for project in my_projects:
    print(f"Project Name:{project['name']}\n Project Url:{project['path']}\n")
    a=project['web_url']
    cur.execute('''INSERT INTO Projects (Path,Project)
                    VALUES (?,0)''',(a,))

    conn.commit()

cur.close()