# ICT2103-SmartPantry
## Tutorial 1 Group 28
Group Members:
1. Jimeno Johanna Charissa Mortel
2. Carlton Anthoni Foo
3. Chang Zhi Jian
4. Tan Zhen Xuan
5. Ong Sheng Wei Kenrick
 
<br />

# Getting Started (for windows)

Make sure you have at least Python 3.9 and Node 14.18 installed

1. Clone the repo to anywhere you want
2. Run your local MySQL Server instance and MySQL Workbench.
3. Import db and tables by importing the '''Objects/sql_scripts/full_script.sql''' file.
4. To install and run the project, run:
    ```
    1. py -3.9 -m venv venv
    2. venv\Scripts\activate 
    3. pip install -r requirements.txt
    4. flask run --host=0.0.0.0 --port=5000
    ```
5. The application should be live on http://localhost:5000
6. Refer to [this webpage](https://appseed.us/admin-dashboards/flask-gradient-able) and [this repo](https://github.com/app-generator/flask-gradient-able) for the structure of this repo.

<br />

# Notes
- Ensure virtual environment (venv) is enabled before staring the project with ```py -3.9 -m venv venv```. If need to, you can disable it with ```deactivate```
- Ensure .env file is present with correct configurations
- Run ``` flask run --host=0.0.0.0 --port=5000 ``` to start the project
- Jiayous guys :')

# .env
The .env file will have 4 variables:
1. FLASK_APP=run.py
2. FLASK_ENV=development
3. SQL_USERNAME=\<mysql username\>
4. SQL_PASSWORD=\<mysql password\>
