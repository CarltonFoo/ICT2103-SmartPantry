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
2. To install the frontend and backend dependencies, cd into the folder and run:

    ```
    npm install
    ```
3. Ignore the warnings when installing
4. To run the project, run:
    ```
    npm run dev
    ```

5. The application should be live on http://localhost:3000
6. Refer to [this webpage](https://dev.to/dev_elie/connecting-a-react-frontend-to-a-flask-backend-h1o) and [this repo](https://github.com/Dev-Elie/Connecting-React-Frontend-to-a-Flask-Backend) for the structure of this repo.

<br />

# Notes
For now, I've set the db to read from backend/database.db . This can be changed to other database sources by editing the ```app.config["SQLALCHEMY_DATABASE_URI"]``` line in backend/app.py . Documentation for this can be found [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/).

If for some reason the installation fails, here are the commands to install and run the frontend and backend:

/frontend
1. cd into /frontend
2. Run ```npm install```
3. Let installation complete
4. Run ```npm start``` to start the frontend

/backend
1. cd into /backend
2. Run the following commands in order (commands will be different for mac/linux). Make sure venv is activated when installing or running:
```
py -3.9 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install mysqlclient-1.4.6-cp39-cp39-win_amd64.whl
```
3. Run ```python routes.py``` while in venv to start the backend (if need to, you can disable venv by running ```deactivate```).


<br />

# Splitting Work
- Create your own branch to work on your parts, please don't work on main branch.
