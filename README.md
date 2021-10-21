# ICT2103-SmartPantry
## Tutorial 1 Group 28
Group Members:
1. Jimeno Johanna Charissa Mortel
2. Carlton Anthoni Foo
3. Chang Zhi Jian
4. Tan Zhen Xuan
5. Ong Sheng Wei Kenrick
 
<br />

# Getting Started

<!-- 1. Download and install XAMPP [here](https://www.apachefriends.org/download.html)
2. Run Apache and MySQL -->
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

<br />

# Splitting Work
- Create your own branch to work on your parts, please don't work on main branch.
