from flask import Blueprint

mysqlbp = Blueprint(
    'mysql_blueprint',
    __name__,
    url_prefix='/mysql'
)

nosqlbp = Blueprint(
    'nosql_blueprint',
    __name__,
    url_prefix='/nosql'
)
