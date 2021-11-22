from apps.home import blueprint
from flask import render_template, request
from flask_login import (
    current_user, 
    login_required 
)
from jinja2 import TemplateNotFound
from Controls.queryControl import queryingOn
# temp
from Objects.sql_commands import mydb
from apps.authentication.util import hash_pass
from apps.authentication.models import Users

@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>', methods=['GET', 'POST'])
@login_required
def route_template(template):
    
    try:
        
        if not template.endswith('.html'):
            template += '.html'
            
        if template == "profile.html":
            selection = "*"
            where = "username ='" + str(current_user) + "'"
            data = queryingOn(method="SELECT", selection=selection, table_name="user", data=where)
            print(data)
        
        if template == "recipes.html":
            data = [("dummy data")]
            
        if template == "inventory.html":
            data = [("dummy data")]
            
        if template == "pricechecker.html":
            data = [("dummy data")]
            
        if template == "budgeting.html":
            data = [("dummy data")]
            
        if template == "history.html":
            data = [("dummy data")]
        
        if template == "aboutus.html":
            data = [("dummy data")]


        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, data=data)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def saveDetails():
    print("clicked")
    if request.method == 'POST':
        if request.form['username']:
            user = Users.query.filter_by(username=request.form['username']).first()
            if not user:
                username = str(request.form['username'])
                height = str(request.form['height'])
                weight = str(request.form['weight'])
                age = str(request.form['age'])
                gender = str(request.form['gender'])
                bio = str(request.form['bio'])
                diet = str(request.form['diet'])
                
                sql = 'UPDATE user SET username = "' + username + '", height = ' + height + ', weight = ' + weight + ', age = ' + \
                    age + ', gender = "' + gender + '", profile_bio = "' + bio + \
                    '", dietary_needs = "' + diet + \
                    '" WHERE username = "' + str(current_user) + '";'
                print(sql)
                
                if request.form['password']:
                    password = str(request.form['password'])
                    passhash = str(hash_pass(password)).split("'")[1]
                    
                    sql = 'UPDATE user SET username = "' + username + '", password = "' + str(passhash) + '", height = ' + height + ', weight = ' + weight + ', age = ' + \
                        age + ', gender = "' + gender + '", profile_bio = "' + bio + \
                        '", dietary_needs = "' + diet + \
                        '" WHERE username = "' + str(current_user) + '";'
                    print(sql)

                mycursor = mydb.cursor()
                mycursor.execute(sql)
                mydb.commit()

                selection = "*"
                where = "username ='" + str(current_user) + "'"
                data = queryingOn(method="SELECT", selection=selection,
                                table_name="user", data=where)
                result = "Profile updated successfully!"
                    
            else:
                selection = "*"
                where = "username ='" + str(current_user) + "'"
                data = queryingOn(method="SELECT", selection=selection, table_name="user", data=where)
                result = "Username exists"

            print(result)
            return render_template('home/profile.html', data=data)



# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
