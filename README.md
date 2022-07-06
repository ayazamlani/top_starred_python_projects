

# Top Starred Python Projects

## About

Uses the GitHub API to retrieve the most starred public Python projects.
Stores the list of repositories in a SQL database table with their respective repository ID, name, URL, created date, last push date, description, and number of stars.



![ListView](https://cdn.imgchest.com/files/w7pjc5x8v7p.png)



![DetailView](https://cdn.imgchest.com/files/d7ogc58q2y9.png)

<hr>

**Built With**

 - Django
 - Tailwind CSS
<hr>

## Getting Started
To get a local copy up and running, please follow these simple steps.

**Pre-requisites**
1. Create a virtual environment
```python -m venv top_starred_python_projects```

2. Enter the environment
    ```cd top_starred_python_projects```
3. Activate the environment
    Windows:
    ```Scripts\activate```
	Mac:
	```source venv/bin/activate```
4. Copy src Folder in to your new environment folder
    ```git pull https://github.com/ayazamlani/top_starred_python_projects.git```

![new environment dir](https://cdn.imgchest.com/files/j7kzc5eoq7m.png)
5. Enter the src directory
    ```cd src```

**Installation**

 1. Install all of the necessary libraries
```pip install -r requirements.txt```

2. Enter the project
```cd python_projects```

3. Create the SQL DB
```python manage.py makemigrations```
```python manage.py migrate```

4. Start the dev server!
 ``` python manage.py runserver ```

5. In your browser, navigate to http://localhost:8000

**Configuration**
To change the number of results per page, Enter the main app folder and edit the settings .py file.
```cd python_projects```
At the bottom of settings .py change the GITHUB_REPOSITORY_RESULTS_PER_PAGE variable
![Github results per page](https://cdn.imgchest.com/files/my2pcz9xw7j.png)
