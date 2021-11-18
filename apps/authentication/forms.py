from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField, DecimalField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

# login and registration


class LoginForm(FlaskForm):
    username = TextField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):    
    username = TextField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    gender = SelectField('Gender',
                             id='gender_create',
                             choices=[('M'), ('F')])
    age = IntegerField('Age',
                             id='age_create'
                             )
    height = DecimalField('Height',
                             id='height_create'
                             )
    weight = DecimalField('Weight',
                             id='weight_create'
                             )
    dietary_needs = TextAreaField('Dietary Needs',
                             id='diet_create'
                             )
    profile_bio = TextAreaField('Profile Bio',
                             id='bio_create'
                             )
