from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

class FoodItems(db.Model):
    __tablename__ = 'food_item'
    fid = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(255))
    price = db.Column(db.Float)
    weight = db.Column(db.Float)
    calories= db.Column(db.Integer)
class Receipts(db.Model):
    __tablename__ = 'receipt'
    rid =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(255))
    calories=  db.Column(db.Integer)
    description= db.Column(db.String(255))
    dietary_needs= db.Column(db.String(255))
class Receipts_Ingredient(db.Model):
    __tablename__ = 'receipt_ingredient'
    rid =db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.String(255))
    weight = db.Column(db.Float)

class pantry(db.Model):
    __tablename__ = 'pantry'

    id = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.FLOAT())


class Users(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    gender = db.Column(db.String(1))
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    dietary_needs = db.Column(db.String(255))
    profile_bio = db.Column(db.String(255))
    

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None



